from typing import Optional

from pydantic import BaseModel

class Tab(BaseModel):
    id: str
    title: str
    artist: str
    content: str

class TabCreate(BaseModel):
    title: str
    artist: str
    content: str

class TabUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    content: Optional[str] = None
