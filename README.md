# AIOps Platform — Day 1

This stage only confirms that a React frontend and FastAPI backend run locally.

## Backend terminal (Command Prompt)

```cmd
cd backend
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`, `http://127.0.0.1:8000/health`, or `http://127.0.0.1:8000/docs`.

## Frontend terminal (Command Prompt)

```cmd
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.
