from fastapi import APIRouter, HTTPException
from app.models.tabs import Tab, TabCreate

from app.databaseConnection import retrieve_all_tabs, add_tab



router = APIRouter()


@router.get("/tabs", response_model=list[Tab])
async def get_tabs() -> list:
    print("in tabs get")
    tabs = await retrieve_all_tabs()
    if not tabs:
        raise HTTPException(status_code=404, detail="No tabs found")
    return tabs


@router.post("/tabs", response_model=Tab)
async def create_tab(tab: TabCreate) -> dict:
    print("hi")
    new_tab = await add_tab(tab.dict())
    return new_tab
