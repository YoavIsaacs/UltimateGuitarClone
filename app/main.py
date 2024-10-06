from fastapi import FastAPI
from .routers import tabs

app = FastAPI()
app.include_router(tabs.router)

@app.get("/")
def home() -> dict:
    return {
        "hello": "world"
    }
