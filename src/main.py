from fastapi import FastAPI


from src.db.database import engine
from src.db import models

app = FastAPI()

@app.get('/')
def index():
    return {'message':'welcome to my travel blog site'}

models.Base.metadata.create_all(engine)