from passlib.context import CryptContext

passwordContext = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashPassword(password: str):
    return passwordContext.hash(password)