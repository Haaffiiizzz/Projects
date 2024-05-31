from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import os
import json

jsonPath = os.path.join(os.getcwd(),'countries.json')
with open(jsonPath, "r") as file:
    data = json.load(file)


app = FastAPI()

class AddData(BaseModel):
    #  this makes sure we are getting the right data format else it
    # throws and error
    country: str
    price: dict


@app.get("/")
def root():
    # this is the base site without any paths
    return {"message": "Welcome to my API"}

@app.get("/countries")
def getPrices():
    #  in this path we should return a json of all the countries
    #  and their items and prices
    return data

@app.get("/countries/{country}")
def getCountryPrices(country: str):
    #  in this path we should return a json of just a country
    #  and its items and prices
    return data[country]

@app.post("/addprice")
def addPrice(newData: AddData):
    #  first check to make sure we have the right data format
    #  send back to user and print data
    print(newData)
    return {"added price": newData}


