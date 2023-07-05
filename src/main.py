from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message':'welcome to my travel blog site'}