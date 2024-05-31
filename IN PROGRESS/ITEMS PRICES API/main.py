from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

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

@app.get("/allprices")
def getPrices():
    #  in this path we shouild return a json of all the countries
    #  and their items and prices
    return {"Country": "Price"}

@app.post("/addprice")
def addPrice(newData: AddData):
    #  first check to make sure we have the right data format
    #  send back to user and print data
    print(newData)
    return {"added price": newData}


