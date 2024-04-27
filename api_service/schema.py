from pydantic import BaseModel
from datetime import date
from .database.db import SessionLocal
from sqlalchemy.orm import sessionmaker


class Vehicle(BaseModel):

    chassis: str
    libre: str
    renewal_date: date


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()