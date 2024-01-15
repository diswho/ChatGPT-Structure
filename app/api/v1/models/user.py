# app/models.py
from sqlalchemy import Column, Integer, String
from app.db.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    email = Column(String)

# Other models can be defined here if needed
