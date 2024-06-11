from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserLogin
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import models
import utils
import oauth2

router = APIRouter(tags = ["Authentication"])

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    
    accessToken = oauth2.createToken(data = {"user_id": user.id})
    return {"Access Token": accessToken, "Token type": "bearer"}