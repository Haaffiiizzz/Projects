from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class AddData(BaseModel):
    #  this makes sure we are getting the right data format else it
    # throws an error
    items: dict

class CreateUser(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    email: EmailStr
    id: int
    createdAt: datetime


    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None