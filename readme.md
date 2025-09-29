# FastApiManagement Assignment

A simple **FastAPI** project for managing users and sessions, with **API key authentication** and **JSON-based session storage**.

---

## ✨ Features
- ✅ Home route (`/`)
- ✅ Get all users (`/getusers`)
- ✅ Add user with API key protection (`/adduser`)
- ✅ Session storage in JSON file (`database/session/sessions.json`)
- ✅ Environment-based secrets using `.env`
- ✅ Modularized utilities (`auth_utils.py`, `session_utils.py`, `libraries.py`)

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the project
```bash
git clone <your-repo-url>
cd Fast_Assignment
````

### 2️⃣ Create & activate a virtual environment

* **Windows (cmd):**

  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **Windows (PowerShell):**

  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

> ✅ You’ll know it’s active if `(venv)` appears in your terminal.

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Create a `.env` file in the root directory:

```
API_KEY=your_secret_api_key
SECRET_KEY=your_flask_secret_key
```

### 5️⃣ Run the server

```bash
uvicorn main:app --reload --port 5000
```

Server will run at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📌 API Endpoints

### 🏠 Home

```http
GET /
```

Response:

```
Home Route
```

### 👥 Get Users

```http
GET /getusers
```

Response:

```json
[
  {
    "id": 1,
    "name": "Ali Khan",
    "age": 24,
    "gender": "male"
  },
  {
    "id": 2,
    "name": "Sara Ahmed",
    "age": 22,
    "gender": "female"
  }
]
```

### ➕ Add User (Protected)

```http
POST /adduser
Headers:
  Content-Type: application/json
  API-KEY: your_secret_api_key
```

Body:

```json
{
  "name": "Fatima Noor",
  "age": 23,
  "gender": "female"
}
```

Response:

```json
{
  "message": "User info saved",
  "session_id": "d0fa7e2e-3d84-4b83-89c1-7e1f5e882abc"
}
```

---

## 📂 Project Structure

```
Fast_Assignment/
│── main.py               # Main FastAPI app
│── auth_utils.py         # API key authentication
│── session_utils.py      # Session file management
│── libraries.py          # Explanation of libraries used
│── data/
│   └── users.json        # User data file
│── database/
│   └── session/
│       └── sessions.json # Session data storage
│── .env                  # Environment variables
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```

---

## 📖 Notes

* `.env` and `venv/` should **not** be pushed to GitHub (add them to `.gitignore`).
* Sessions are stored in `database/session/sessions.json`.
* API requires the correct `API-KEY` header for protected routes.

---

## 🧾 What is `.md`?

`.md` stands for **Markdown**, a lightweight markup language used for formatting text.
It allows you to create **styled documentation** with headings, lists, code blocks, links, etc.

---

✅ Now your project has a **full professional README**!

Do you also want me to generate the `.gitignore` file for you so that `venv/` and `.env` don’t accidentally get pushed?
