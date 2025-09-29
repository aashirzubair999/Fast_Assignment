from fastapi import Request, HTTPException, status
from .config import API_KEY

def api_key_required(request: Request):
    """FastAPI dependency to require header 'API-KEY'."""
    key = request.headers.get("API-KEY")
    if not key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API key required")
    if API_KEY is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server API_KEY not configured")
    if key != API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized")
    return True
