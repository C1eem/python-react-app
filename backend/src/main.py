from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.users.router import router as user_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  # ← важно
    allow_headers=["*"],  # ← и это тоже
)
app.include_router(user_router)
