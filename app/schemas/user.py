from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int

class UserInDB(UserBase):
    id: int
    hashed_password: str

    class Config:
        orm_mode = True
