from fastapi import FastAPI, status, HTTPException, Body, Depends
import psycopg2
from psycopg2.extras import RealDictCursor
from database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy import Table, MetaData
from contextlib import contextmanager
import schemas
import models
from utils import hashPassword


app = FastAPI()

metadata = MetaData()
countriesTable = Table('Countries1', metadata, autoload_with=engine)

password = open(r"C:\Users\dadaa\OneDrive\Desktop\password.txt", "r").read()
password = password.strip()

models.Base.metadata.create_all(bind=engine)

@contextmanager
def psycopg2Cursor():

    conn = psycopg2.connect(
    dbname="ItemsAPI",
    user="postgres",
    password=password,
    host="localhost",
    port="5432",
    cursor_factory=RealDictCursor
    )
    try:
        cursor = conn.cursor()
        yield cursor
        conn.commit()
    
    except Exception as Ex:
        conn.rollback()
        raise Ex
    
    finally:
        cursor.close()
        conn.close()


@app.get("/")
def root(db: Session = Depends(get_db)):
    # this is the base site without any paths

    countries = db.query(countriesTable).all()
    countryNames = [row.name for row in countries]
    return {"message": f"Welcome to my Items API. Below is a list of all countries available.",
            "countries": countryNames}


@app.get("/countries")
def getPrices(db: Session = Depends(get_db)):

    countries = db.query(countriesTable).all()
    result = [{column.name: getattr(row, column.name) for column in countriesTable.columns} for row in countries]
    # result is a list of dicts, with each cloumn name in the table as key
    # and the items in the columns as values
    resultDict = {}
    for Dict in result:
        name = Dict["name"]
        itemsDict = {key:value for key, value in Dict.items() if key != "name"}
        resultDict[name] = itemsDict

    return resultDict


@app.get("/countries/{country}")
def getCountryPrices(country: str, db: Session = Depends(get_db)):
    #  in this path we should return a json of just a country
    #  and its items and prices
    country = country.title()

    row = db.query(countriesTable).filter(countriesTable.c.name == country).first()
    #  check if the row is valid i.e country in data base else raise error
    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{country} not found")
    #  format the data
    rowDict = {column: value for column, value in zip(countriesTable.columns.keys(), row)}
    items = {key: value for key, value in rowDict.items() if key != 'name'}
    return {"Country": country, "Items": items}


@app.put("/countries/{country}", status_code=status.HTTP_201_CREATED)
def addPrice(country, newData: schemas.AddData = Body(...)):
    #  first check to make sure we have the right data format
    #  send back to user and print data
    country = country.title()
    with psycopg2Cursor() as cursor:
        cursor.execute(f'SELECT * FROM "Countries1" WHERE name = \'{country}\';')
        row = cursor.fetchone()

        if not row:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"{country} not found")
        # check i fthe row is valid i.e the country is in the database
        
        for itemName in newData.items.keys():
            cursor.execute(f"""
                DO $$
                BEGIN
                    IF NOT EXISTS (
                        SELECT 1
                        FROM information_schema.columns 
                        WHERE table_name='Countries1' AND column_name= \'{itemName}\'
                    ) THEN
                        ALTER TABLE "Countries1" ADD COLUMN "{itemName}" NUMERIC;
                    END IF;
                END
                $$;
            """)
        
        #  create new row with the name of the item if the row is not already available
        #  note: null will be the value
        
        for itemName, itemPrice in newData.items.items():
            cursor.execute(
                f'UPDATE "Countries1" SET "{itemName}" = %s WHERE name = %s;',
                (itemPrice, country)
            )
        
    # update the database i.e replace null with the right stuff
    
    return {"Added prices": {"Country" : country.title(), "items": newData.items()}}


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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, reload_dirs=['/app'])
