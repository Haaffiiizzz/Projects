from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


password = open("password.txt", "r").read()
password = password.strip()

SQL_DB_URL = f"postgresql://postgres:{password}@localhost/ItemsAPI"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQL_DB_URL)

localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine) 

Base = declarative_base()