from fastapi import APIRouter, Depends

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
