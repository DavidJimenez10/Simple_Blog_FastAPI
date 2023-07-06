from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

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

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)