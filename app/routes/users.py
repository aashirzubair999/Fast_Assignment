import uuid
import json
from fastapi import APIRouter, HTTPException, Response, Depends
from fastapi.responses import JSONResponse, PlainTextResponse

from app.models import AddUserIn, SessionRequest
from app.core.auth_utils import api_key_required
from app.core.session_utils import session_dict, save_sessions
from app.core.config import DATA_FILE

from pathlib import Path

router = APIRouter()

# Ensure data file exists
DATA_FILE = Path(DATA_FILE)
if not DATA_FILE.exists():
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text("[]")


@router.get("/", response_class=PlainTextResponse)
def home():
    return "Home Route"


@router.get("/getusers")
def get_users():
    try:
        if not DATA_FILE.exists():
            return JSONResponse(status_code=200, content=[])
        with DATA_FILE.open("r", encoding="utf-8") as f:
            users = json.load(f)
            return PlainTextResponse(json.dumps(users, indent=4))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error using user file {e}")


@router.post("/adduser", status_code=201)
async def add_user(payload: AddUserIn, response: Response, authorized: bool = Depends(api_key_required)):
    try:
        session_id = str(uuid.uuid4())
        session_dict[session_id] = {
            "name": payload.name,
            "age": payload.age,
            "gender": payload.gender
        }
        save_sessions()
        response.set_cookie(key="session_id", value=session_id, httponly=True)
        return {"message": "User info saved", "session_id": session_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding user: {e}")


@router.post("/getuserthroughsession")
async def get_user_through_session(payload: SessionRequest, authorized: bool = Depends(api_key_required)):
    try:
        session_id = payload.session_id
        user = session_dict.get(session_id)
        if not user:
            raise HTTPException(status_code=404, detail="Invalid session ID")
        return {"user": user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
