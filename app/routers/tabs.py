from fastapi import APIRouter, HTTPException
from ..models.tabs import Tab
from ..databaseConnection import retrieve_all_tabs


router = APIRouter()


@router.get("/tabs", response_model=list[Tab])
async def get_tabs() -> list:
    tabs = await retrieve_all_tabs()
    if not tabs:
        raise HTTPException(status_code=404, detail="No tabs found")
    return tabs


