# main.py
# cors fix only
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ── CORS ────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # z. B. React/Vite
        "http://127.0.0.1:3000",
        "http://localhost:5173",  # Vite default
        "http://127.0.0.1:5173",
        "http://localhost:*",  # wenn du verschiedene Ports testest
        "*",  # ← oder einfach alles erlauben (nur dev!)
    ],
    allow_credentials=True,  # falls du später Cookies brauchst
    allow_methods=["*"],  # GET, POST, PUT, DELETE, OPTIONS, ...
    allow_headers=["*"],
)
