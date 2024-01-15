# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from app.api.v1.main import router as v1_router
from app.api.v1.dependencies.auth import get_current_user
from app.core.config import settings

app = FastAPI()

if settings.debug:
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(v1_router, prefix="/v1", tags=["v1"])


@app.get("/secure-endpoint", dependencies=[Depends(get_current_user)])
async def secure_endpoint(current_user: dict = Depends(get_current_user)):
    return {"message": "You have access to this secure endpoint!", "username": current_user["username"]}
