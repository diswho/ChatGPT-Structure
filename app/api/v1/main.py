# app/api/v1/main.py
from fastapi import APIRouter
from .routers import users,token

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(token.router, prefix="/token", tags=["token"])

# @router.get("/")
# async def read_root():
#     return {"message": "Hello, API v1!"}
