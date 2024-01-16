# app/api/v1/models/user.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base

class UserResponseModel(Base):
    username: str
    email: str

class UserModel(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String)
