import os
import json

# Path to the session file (make sure this matches your folder)
session_file = "database/session/session.json"

# Ensure the folder exists
if not os.path.exists(os.path.dirname(session_file)):
    os.makedirs(os.path.dirname(session_file), exist_ok=True)

# Load existing sessions or initialize an empty dict
try:
    with open(session_file, "r") as f:
        session_dict = json.load(f)
except FileNotFoundError:
    print(f"Session file not found: {session_file}. Initializing empty sessions.")
    session_dict = {}

# Utility function to save sessions back to file
def save_sessions():
    try:
        with open(session_file, "w") as f:
            json.dump(session_dict, f, indent=4)
    except Exception as e:
        print("Error saving sessions:", e)
