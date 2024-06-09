from pydantic import BaseModel

class AddData(BaseModel):
    #  this makes sure we are getting the right data format else it
    # throws and error
    items: dict