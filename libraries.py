from fastapi import FastAPI, Request, Response, Depends, HTTPException, status
from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from dotenv import load_dotenv
import json, uuid
from pydantic import BaseModel

from session_utils import session_dict, save_sessions
from auth_utils import api_key_required


