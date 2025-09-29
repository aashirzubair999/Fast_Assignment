import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
DATA_FILE = "data/users.json"
SESSION_FILE = "database/session/session.json"
