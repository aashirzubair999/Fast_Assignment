import os
import json
from .config import SESSION_FILE

# Ensure session folder exists
os.makedirs(os.path.dirname(SESSION_FILE), exist_ok=True)

# Load existing sessions or start fresh
try:
    with open(SESSION_FILE, "r") as f:
        session_dict = json.load(f)
except FileNotFoundError:
    session_dict = {}

def save_sessions():
    """Save sessions back to file"""
    try:
        with open(SESSION_FILE, "w") as f:
            json.dump(session_dict, f, indent=4)
    except Exception as e:
        print("Error saving sessions:", e)
