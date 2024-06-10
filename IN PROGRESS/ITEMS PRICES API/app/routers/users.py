from fastapi import FastAPI, status, HTTPException, Body, Depends
from database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy import Table, MetaData
import schemas
import models
from utils import hashPassword


app = FastAPI()

metadata = MetaData()
countriesTable = Table('Countries1', metadata, autoload_with=engine)

password = open(r"C:\Users\dadaa\OneDrive\Desktop\password.txt", "r").read()
password = password.strip()

models.Base.metadata.create_all(bind=engine)

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def createUser(user: schemas.CreateUser, db: Session = Depends(get_db)):
    
    hashedPassword = hashPassword(user.password)
    user.password = hashedPassword
    newUser = models.User(**user.dict())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser


@app.get("/users/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def getUser(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with {id} not found")

    return user