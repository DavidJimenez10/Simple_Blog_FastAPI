from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.db.database import engine
from src.db import models
from src.routers import post
from src.config import config

app = FastAPI()
app.include_router(post.router)

@app.get('/')
def index():
    return {'message':'welcome to my travel blog site'}

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory=config.folder_static_images), name='images')
