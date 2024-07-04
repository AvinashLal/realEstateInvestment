from fastapi import FastAPI
from app.routes import item

app = FastAPI()

app.include_router(item.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
