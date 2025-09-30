from fastapi import Request, HTTPException, status
from .config import API_KEY

def api_key_required(request: Request):
    """FastAPI dependency to require header 'API-KEY'."""
    key = request.headers.get("API-KEY")
    # Check if the key is present and valid
    if not key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API key required")
    # Check if the key matches the server's API_KEY
    if API_KEY is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server API_KEY not configured")
    # Check if the key matches the server's API_KEY
    if key != API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized")
    return True
