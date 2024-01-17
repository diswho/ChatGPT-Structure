from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud.user import create_user, get_users
from app.schemas.user import UserCreate, UserOut
from app.core.database import SessionLocalInternal
from app.api.v1.endpoints.auth import get_current_user
from app.models.user import User
from app.utils.security import pwd_context

router = APIRouter()

@router.post("/users/", response_model=UserOut)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(SessionLocalInternal),
    current_user: User = Depends(get_current_user),
):
    hashed_password = pwd_context.hash(user.password)
    db_user = create_user(db, user, hashed_password)
    return db_user
