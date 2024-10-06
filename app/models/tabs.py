from pydantic import BaseModel

class Tab(BaseModel):
    id: str
    title: str
    artist: str
    content: str