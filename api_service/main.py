from fastapi import FastAPI
from . api import end_points
from .database import models, db

app = FastAPI()

models.Base.metadata.create_all(db.engine)

app.include_router(end_points.router)

