from libraries import *

load_dotenv()

app = FastAPI(title="FastApiManagement Assignment")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True
)


class AddUserIn(BaseModel):
    name: str
    age: int
    gender: str

class SessionRequest(BaseModel):
    session_id: str


DATA_FILE = Path("data/users.json")
if not DATA_FILE.exists():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text("[]")


# 1) Home route
@app.get("/", response_class=PlainTextResponse)
def home():
    return "Home Route"


# 2) Get all users
@app.get("/getusers")
def get_users():
    try:
        if not DATA_FILE.exists():   
            return JSONResponse(status_code=200, content=[])
        with DATA_FILE.open("r", encoding="utf-8") as f:
            users = json.load(f)
            return PlainTextResponse(json.dumps(users, indent=4))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error using user file {e}")

# 3) Add Users
@app.post("/adduser", status_code=201)
async def add_user(payload: AddUserIn, response: Response, authorized: bool = Depends(api_key_required)):
    try:
        session_id = str(uuid.uuid4())
        session_dict[session_id] ={
            "name": payload.name,
            "age": payload.age,
            "gender": payload.gender
            }
        save_sessions()
        response.set_cookie(key="session_id", value=session_id, httponly=True)
        return {"message": "User info saved", "session_id": session_id}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding user: {e}")

# 4) Get User by Session ID
@app.post("/getuserthroughsession")
async def get_user_through_session(payload: SessionRequest, authorized: bool = Depends(api_key_required)):
    try:
        session_id = payload.session_id
        user = session_dict.get(session_id)
        if not user:
            raise HTTPException(status_code=404, detail="Invalid session ID")
        return {"user": user}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    