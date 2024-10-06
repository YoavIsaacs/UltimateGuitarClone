from fastapi import FastAPI
from app.routers.tabs import tabs_router
from app.routers.auth import auth_router

app = FastAPI()
app.include_router(tabs_router)
app.include_router(auth_router)

@app.get("/")
def home() -> dict:
    return {
        "hello": "world"
    }
