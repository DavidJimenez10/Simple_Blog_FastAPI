from fastapi import APIRouter, Depends, UploadFile, File

from typing import List
import string
import random
import shutil

from sqlalchemy.orm.session import Session

from src.schema import PostBase, PostDisplay
from src.db.models import DbPost
from src.db.database import get_db
from src.db import db_post
from src.config import config


router = APIRouter(
    prefix = '/post',
    tags = ['post']
)


@router.post('/new', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create_post(db, request)


@router.get('/all', response_model=List[PostDisplay])
def get_all(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/delete/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    return db_post.delete_post(db, id)

@router.post('/image')
def upload_img(image: UploadFile = File(...)):
    
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))

    filename = f'_{rand_str}.'.join(image.filename.rsplit('.',1))
    path = f'{config.folder_static_images}{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': f'{config.mount_images}/{filename}'}