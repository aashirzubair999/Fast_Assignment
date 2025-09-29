from fastapi import Request, HTTPException, status
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def api_key_required(request: Request):
    """FastAPI dependency to require header 'API-KEY'."""
    key = request.headers.get("API-KEY")
    # Debugging print (remove in production)
    print("Received API-KEY:", key)
    if not key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API key required")
    if API_KEY is None:
        # Environment misconfiguration
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server API_KEY not configured")
    if key != API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized")
    # If valid, return None — dependency fulfilled
    return True
