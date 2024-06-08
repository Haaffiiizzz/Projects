from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


password = open(r"C:\Users\dadaa\OneDrive\Desktop\password.txt", "r").read()
password = password.strip()

SQL_DB_URL = f"postgresql://postgres:{password}@localhost/ItemsAPI"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQL_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
        
    finally:
        db.close()


