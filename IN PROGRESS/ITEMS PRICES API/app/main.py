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
    return {"message": f"Welcome to my API. Below is a list of all countries available.",
            "countries": [key for key in data.keys()]}


@app.get("/countries")
def getPrices():
    #  in this path we should return a json of all the countries
    #  and their items and prices
    return {"countries": data}

@app.get("/countries/{country}")
def getCountryPrices(country: str):
    #  in this path we should return a json of just a country
    #  and its items and prices
    if country.title() not in data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{country} not found")
    return {"country": data[country.title()]}


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


