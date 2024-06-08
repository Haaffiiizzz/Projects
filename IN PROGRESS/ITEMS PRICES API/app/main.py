from fastapi import FastAPI, status, HTTPException, Body, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import models
from database import engine, Base, get_db
from sqlalchemy.orm import Session 
from sqlalchemy import Table, MetaData


app = FastAPI()

metadata = MetaData()
countriesTable = Table('Countries1', metadata, autoload_with=engine)

password = open(r"C:\Users\dadaa\OneDrive\Desktop\password.txt", "r").read()
password = password.strip()
try:
    conn = psycopg2.connect(
    dbname="ItemsAPI",
    user="postgres",
    password=password,
    host="localhost",
    port="5432",
    cursor_factory=RealDictCursor
)
    cursor = conn.cursor()
   
except Exception as Ex:
    print("Error", Ex.args[0])




class AddData(BaseModel):
    #  this makes sure we are getting the right data format else it
    # throws and error
    items: dict

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

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

@app.get("/")
def root():
    # this is the base site without any paths

    cursor.execute('SELECT name FROM "Countries";')
    countries = cursor.fetchall()
    countryNames = [country['name'] for country in countries]  # basically saying for dict in the list of dicts?
    # or dict of dict i think. doesnt matter lol

    return {"message": f"Welcome to my API. Below is a list of all countries available.",
            "countries": countryNames}

    # note: fetch all or fetch one fetch the row(s) as dict
    #  so each row column title as jey, and the row value as values

@app.get("/countries")
def getPrices():
    #  in this path we should return a json of all the countries
    #  and their items and prices
    cursor.execute('SELECT * FROM "Countries";')
    countries = cursor.fetchall()
    # first get the data from the database

    countriesDict = {}
    for row in countries:
        name = row['name']
        items = {key : value for key, value in row.items() if key != 'name'}
        countriesDict[name] = items

    # then format accordingly and return
    return countriesDict

@app.get("/countries/{country}")
def getCountryPrices(country: str):
    #  in this path we should return a json of just a country
    #  and its items and prices
    country = country.title()

    cursor.execute(f'SELECT * FROM "Countries" WHERE name = \'{country}\';')
    row = cursor.fetchone()

    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{country} not found")
    #  check if the row is valid i.e country in data base else raise error
    
    items = {key: value for key, value in row.items() if key != 'name'}
    #  create dict with keys and values from row in database

    return {"Country": country,
            "Items": items}


@app.post("/countries/{country}", status_code=status.HTTP_201_CREATED)
def addPrice(country, newData: AddData = Body(...)):
    #  first check to make sure we have the right data format
    #  send back to user and print data
    country = country.title()
    cursor.execute(f'SELECT * FROM "Countries" WHERE name = \'{country}\';')
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
                    WHERE table_name='Countries' AND column_name= \'{itemName}\'
                ) THEN
                    ALTER TABLE "Countries" ADD COLUMN "{itemName}" NUMERIC;
                END IF;
            END
            $$;
        """)
    
    #  create new row with the name of the item if the row is not already available
    #  note: null will be the value
    
    for itemName, itemPrice in newData.items.items():
        cursor.execute(
            f'UPDATE "Countries" SET "{itemName}" = %s WHERE name = %s;',
            (itemPrice, country)
        )
    
    # update the database i.e replace null with the right stuff
    
    conn.commit()

    return {"Added price": {"Country" : country.title(), "items": newData.items()}}


