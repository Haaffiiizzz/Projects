from fastapi import FastAPI
from database import engine
from sqlalchemy import Table, MetaData
import models
from routers import users, country



metadata = MetaData()
countriesTable = Table('Countries1', metadata, autoload_with=engine)

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(country.router)
app.include_router(users.router)