from database import Base
from sqlalchemy import Column, String, JSON
class Countries(Base):
    __tablename__ = "countries"

    name = Column(String, primary_key = True, nullable =False)
    items = Column(JSON, nullable=False)