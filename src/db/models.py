from sqlalchemy.types import String, Integer, DateTime
from sqlalchemy import Column

from src.db.database import Base

class DbPost(Base):
    __tablename__ = "POST"
    ID = Column(Integer, primary_key=True, index=True)
    TITLE = Column(String)
    CREATOR = Column(String)
    CONTENT = Column(String)
    IMAGE_URL = Column(String)
    TIMESTAMP = Column(DateTime)