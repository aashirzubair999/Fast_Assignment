from pydantic import BaseModel

class AddUserIn(BaseModel):
    name: str
    age: int
    gender: str

class SessionRequest(BaseModel):
    session_id: str
