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

