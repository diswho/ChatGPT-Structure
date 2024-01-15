# app/api/v1/routers/users.py
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.v1.models.user import User
from app.api.v1.dependencies.database import get_db_session
from app.core.security import get_password_hash
from app.api.v1.models import UserModel
from app.api.v1.dependencies.auth import authenticate_user
from app.core.security import create_access_token


router = APIRouter()


@router.post("/create-user/")
async def create_user(user: User, db: Session = Depends(get_db_session)):
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(username=user.username,
                        email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"username": user.username, "email": user.email}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
    user = db.query(UserModel).filter(
        UserModel.username == form_data.username).first()
    if not user or not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}
