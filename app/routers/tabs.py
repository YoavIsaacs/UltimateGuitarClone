from fastapi import APIRouter, HTTPException, Depends

from app.core.dependencies import get_current_user
from app.models.tabs import Tab, TabCreate, TabUpdate

from app.databaseConnection import retrieve_all_tabs, add_tab, update_tab, delete_tab

router = APIRouter(prefix="/tabs")


@router.get("", response_model=list[Tab])
async def get_tabs(current_user: Depends(get_current_user)) -> list:
    print("in tabs get")
    tabs = await retrieve_all_tabs()
    if not tabs:
        raise HTTPException(status_code=404, detail="No tabs found")
    return tabs


@router.post("", response_model=Tab)
async def create_tab(tab: TabCreate) -> dict:
    print("hi")
    new_tab = await add_tab(tab.model_dump())
    return new_tab

@router.patch("/{tab_id}", response_model=Tab)
async def update_tab_in_db(tab_id: str, tab: TabUpdate) -> dict:
    update_data = tab.model_dump(exclude_unset=True)
    updated_tab = await update_tab(tab_id, update_data)
    if not updated_tab:
        raise HTTPException(status_code=404, detail="Tab not found")
    return updated_tab

@router.delete("/{tab_id}", response_model=dict)
async def delete_tab_in_db(tab_id: str) -> dict:
        deleted = await delete_tab(tab_id)

        if not deleted:
            raise HTTPException(status_code=404, detail="Tab not found")
        return {"message": "Tab deleted successfully"}