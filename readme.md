# Fast Assignment – FastAPI Project

This is a simple **FastAPI** application that manages users and sessions with API key authentication.
It demonstrates how to build modular APIs with authentication, session handling, and JSON file storage.

---

## Features

* **FastAPI** backend with modular structure
* **CORS middleware** enabled
* **API Key authentication** (via request header `API-KEY`)
* User management:

  * Add users
  * Get all users
  * Fetch user by session ID
* Sessions stored in `database/session/session.json`
* Environment variables handled with `.env`

---

## Project Structure

```
Fast_Assignment/
│── app/                   # Core application package
│── data/                  # Stores users.json
│── database/
│   └── session/
│       └── session.json   # Stores active sessions
│── fastenv/               # Virtual environment (ignored in Git)
│── main.py                # Entry point (FastAPI app)
│── requirements.txt       # Python dependencies
│── readme.md              # Project documentation
│── .env                   # Environment variables (API_KEY etc.)
│── .gitignore
```

---

## Setup Instructions

### 1️⃣ Clone repository

```bash
git clone https://github.com/aashirzubair999/Fast_Assignment.git
cd Fast_Assignment
```

### Create virtual environment

```bash
python -m venv fastenv
fastenv\Scripts\Activate.py    # On Windows
# OR
source fastenv/bin/activate # On Linux/Mac
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file in the root directory:

```
API_KEY=your_secret_api_key
```

---

## Running the App

Run the server with:

```bash
uvicorn main:app --reload --port 5000
```

Now open:

* Interactive API docs → [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)

---

## Authentication

All protected routes require a header:

```
API-KEY: your_secret_api_key
```

---

##API  Endpoints

### 1) Home

```http
GET /
```

Response:

```
"Home Route"
```

---

### 2) Get all users

```http
GET /getusers
```

Returns list of all users.

---

### 3) Add a new user

```http
POST /adduser
Headers: { "API-KEY": "your_secret_api_key" }
Body (JSON):
{
  "name": "Alice",
  "age": 25,
  "gender": "Female"
}
```

Response:

```json
{
  "message": "User info saved",
  "session_id": "uuid-generated-id"
}
```

---

### 4) Get user by session ID

```http
POST /getuserthroughsessionid
Headers: { "API-KEY": "your_secret_api_key" }
Body (JSON):
{
  "session_id": "uuid-generated-id"
}
```

Response:

```json
{
  "user": {
    "name": "Alice",
    "age": 25,
    "gender": "Female"
  }
}
```

---

## Requirements

All dependencies are listed in `requirements.txt`:

* fastapi
* uvicorn
* python-dotenv

---

## Notes

* Sessions are stored in `database/session/session.json`.
* Users are stored in `data/users.json`.
* Make sure your `.env` contains a valid `API_KEY`.

---
