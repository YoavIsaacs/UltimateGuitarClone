from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.tabs import tabs_router
from app.routers.auth import auth_router

app = FastAPI()
app.include_router(tabs_router)
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home() -> dict:
    return {
        "hello": "world"
    }
