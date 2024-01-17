from sqlalchemy.orm import Session
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from app.core.config import settings
from app.core.database import SessionLocalInternal
# from app.crud.user import get_user_by_email
from app.schemas.user import UserInDB
# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def verify_token(token: str, db: Session = Depends(SessionLocalInternal)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = {"sub": email}
    except JWTError:
        raise credentials_exception
    return token_data
