from pydantic import BaseModel, EmailStr

class AddData(BaseModel):
    #  this makes sure we are getting the right data format else it
    # throws an error
    items: dict

class CreateUser(BaseModel):
    email: EmailStr
    password: str