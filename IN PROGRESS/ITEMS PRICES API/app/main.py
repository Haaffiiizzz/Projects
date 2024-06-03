from fastapi import FastAPI, status, HTTPException, Body
from pydantic import BaseModel
import json
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

file = open(r"C:\Users\dadaa\Projects\IN PROGRESS\ITEMS PRICES API\countries.json", "r")
data = json.load(file)

try:
    conn = psycopg2.connect(
    dbname="ItemsAPI",
    user="postgres",
    password="Jss3ajdssk06.",
    host="localhost",
    port="5432",
    cursor_factory=RealDictCursor
)
    cursor = conn.cursor()
    print("Database connection was successful")
     
except Exception as Ex:
    print("Error", Ex.args[0])


class AddData(BaseModel):
    #  this makes sure we are getting the right data format else it
    # throws and error
    prices: dict


@app.get("/")
def root():
    # this is the base site without any paths
    cursor.execute('SELECT name FROM "Countries";')
    countries = cursor.fetchall()
    country_names = [country['name'] for country in countries]

    return {"message": f"Welcome to my API. Below is a list of all countries available.",
            "countries": country_names}



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
    cursor.execute(f'SELECT * FROM "Countries" WHERE name = \'{country}\';')
    row = cursor.fetchone()

    if not row:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{country} not found")
    
    items = {key: value for key, value in row.items() if key != 'name'}
    return {"Country": country,
            "Items": items}


@app.post("/countries/{country}", status_code=status.HTTP_201_CREATED)
def addPrice(country, newData: AddData = Body(...)):
    #  first check to make sure we have the right data format
    #  send back to user and print data
    if country.title() not in data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{country} not found")
    
    data[country.title()][1].update(newData.prices)    # update the country's price dict with the new items
    
    with open(r"C:\Users\dadaa\Projects\IN PROGRESS\ITEMS PRICES API\countries.json", "w") as file:
        json.dump(data, file, indent=4)

    return {"Added price": {"Country" : country.title(), "items": newData.price}}


