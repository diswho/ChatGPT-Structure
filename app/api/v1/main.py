# app/api/v1/main.py
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Hello, API v1!"}
