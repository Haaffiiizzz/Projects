from jose import JWTError, jwt
from datetime import datetime, timedelta
import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "09d25e094faa6ca2556c81816637a9563b93f7099f6f0f4caa6cf63b88e8d3h7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def createToken(data: dict):
    toEncode= data.copy()

    expire = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    toEncode.update({"exp": expire})

    encodedJWT = jwt.encode(toEncode, SECRET_KEY, algorithm = ALGORITHM)
    return encodedJWT
    # here the token is created using the payload(toEncode), secret key and algorithm

def verifyToken(token: str, credentialsException):
    # this function is only called by getcurrent user which is what we call in the other files
    # we dint call this directly in the other files
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if not id:
            raise credentialsException
        
        token_data = schemas.TokenData(id=str(id))
    
    except JWTError:
        raise credentialsException
    
    return token_data

def getCurrentUser(token: str = Depends(oauth2_scheme)):
    credentialsException = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials"
      , headers = {"WWW-Authenticate": "Bearer"})
   
    return verifyToken(token, credentialsException)