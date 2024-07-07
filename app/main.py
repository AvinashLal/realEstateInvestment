from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.api.v1.endpoints import item


app = FastAPI()
app.include_router(item.router, prefix="/items", tags=["items"])

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(item.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Serve the favicon.ico file
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")