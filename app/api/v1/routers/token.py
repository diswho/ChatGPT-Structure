# app/api/v1/routers/token.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.api.v1.dependencies.auth import authenticate_user
from app.core.security import create_access_token

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_authenticated = authenticate_user(form_data.username, form_data.password)
    if not user_authenticated:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
