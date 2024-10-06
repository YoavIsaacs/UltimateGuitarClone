from fastapi import FastAPI
from app.routers.tabs import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home() -> dict:
    return {
        "hello": "world"
    }
