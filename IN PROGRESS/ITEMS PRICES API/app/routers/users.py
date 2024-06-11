from fastapi import status, HTTPException, Depends, APIRouter
from database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy import Table, MetaData
import schemas
import models
from utils import hashPassword


router = APIRouter(prefix = "/users", tags = ['Users'])

metadata = MetaData()
countriesTable = Table('Countries1', metadata, autoload_with=engine)

models.Base.metadata.create_all(bind=engine)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def Create_User(user: schemas.CreateUser, db: Session = Depends(get_db)):
    
    hashedPassword = hashPassword(user.password)
    user.password = hashedPassword
    newUser = models.User(**user.dict())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser


@router.get("/{id}", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def Get_User(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    return user