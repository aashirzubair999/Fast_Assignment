from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users

app = FastAPI(title="FastApiManagement Assignment")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=False
)

# Register routes
app.include_router(users.router, prefix="", tags=["Users"])
