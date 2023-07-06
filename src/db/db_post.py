from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from src.schema import PostBase
from src.db.models import DbPost

from datetime import datetime

def create_post(db: Session, request: PostBase):
    new_post = DbPost(
        TITLE = request.TITLE,
        CREATOR = request.CREATOR,
        IMAGE_URL = request.IMAGE_URL,
        CONTENT = request.CONTENT,
        TIMESTAMP = datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session):
    return db.query(DbPost).all()

def delete_post(db: Session, id: int):
    post = db.query(DbPost).filter(DbPost.ID == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f'Post with id {id} not found'
            )
    db.delete(post)
    db.commit()
    return 'deleted'