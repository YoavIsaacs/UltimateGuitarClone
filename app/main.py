from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home() -> dict:
    return {
        "hello": "world"
    }
