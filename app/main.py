# app/main.py

from fastapi import FastAPI
from app.routers.conversation import router

app = FastAPI(
    title="Personalized Networking Assistant API"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Personalized Networking Assistant API!"
    }