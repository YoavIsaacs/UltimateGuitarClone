from pydantic import BaseModel

class Tab(BaseModel):
    id: int
    title: str
    artist: str
    content: str