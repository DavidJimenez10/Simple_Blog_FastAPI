from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    TITLE : str
    CREATOR : str
    CONTENT : str
    IMAGE_URL : str

class PostDisplay(BaseModel):
    ID : int    
    TITLE : str
    CREATOR : str
    CONTENT : str
    IMAGE_URL : str
    TIMESTAMP : datetime
    
    class Config():
        orm_mode = True