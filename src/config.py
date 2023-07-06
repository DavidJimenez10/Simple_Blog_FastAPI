from pydantic import BaseSettings

class Config(BaseSettings):
    
    folder_static_images: str = 'src/assets/img/'

config = Config()