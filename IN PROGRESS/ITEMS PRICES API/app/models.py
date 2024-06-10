from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text

class User(Base):
    __tablename__ = "users"
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id = Column(Integer, primary_key= True, nullable=False)
    createdAt = Column(TIMESTAMP(timezone=True), nullable=False, 
                       server_default= text('now()'))

