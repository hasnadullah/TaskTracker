# app/schemas/user_schema.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str  # "intern", "mentor", "hr"

class UserCreate(UserBase):
    password: str  # NOT HASHED (your requirement)

class UserLogin(BaseModel):
    email: EmailStr
    password: str  # plain password

class UserResponse(UserBase):
    id: str

    class Config:
        orm_mode = True
