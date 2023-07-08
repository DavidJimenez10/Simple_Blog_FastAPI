from pydantic import BaseSettings

class Config(BaseSettings):
    
    folder_static_images: str = 'src/assets/img/'
    mount_images: str = '/images'

config = Config()