from sqlalchemy import Date, Column, ForeignKey, Integer, String
from .db import Base
from . import db
from fastapi import FastAPI
from pydantic import BaseModel



class Vehicle(Base):

    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    chassis = Column(String, index=True)
    libre = Column(String, index=True)
    renewal_date = Column(Date)

    




