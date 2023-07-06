from fastapi import APIRouter, Depends

from typing import List

from sqlalchemy.orm.session import Session

from src.schema import PostBase, PostDisplay
from src.db.models import DbPost
from src.db.database import get_db
from src.db import db_post


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

@router.get('/delete/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    return db_post.delete_post(db, id)