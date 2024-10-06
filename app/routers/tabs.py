from fastapi import APIRouter
from ..models.tabs import Tab


router = APIRouter()

# Temporary list of tabs until mongo integration
tabs = [
    Tab(id=1, title="Wonderwall", artist="Oasis", content="Chords for Wonderwall..."),
    Tab(id=2, title="Hotel California", artist="Eagles", content="Chords for Hotel California..."),
]

@router.get("/tabs", response_model=list[Tab])
def get_tabs() -> list:
    return tabs

