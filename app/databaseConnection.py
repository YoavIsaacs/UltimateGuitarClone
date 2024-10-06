from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/ultimate_guitar_clone")
client = AsyncIOMotorClient(MONGO_URI)
database = client["ultimate_guitar_clone"]
tab_collection = database.get_collection("tabs")


async def retrieve_all_tabs() -> list:
    tabs = []
    async for tab in tab_collection.find():
        tabs.append({
            "id": str(tab["_id"]),
            "title": tab["title"],
            "artist": tab["artist"],
            "content": tab["content"]
        })

    return tabs


async def add_tab(tab_data: dict) -> dict:
    tab = await tab_collection.insert_one(tab_data)
    new_tab = await tab_collection.find_one({"_id": tab.inserted_id})
    return {
        "id": str(new_tab["_id"]),
        "title": new_tab["title"],
        "artist": new_tab["artist"],
        "content": new_tab["content"]
    }

async def update_tab(tab_id: str, tab_data: dict):
    if not ObjectId.is_valid(tab_id):
        return None

    updated = await tab_collection.update_one(
        {
            "_id": ObjectId(tab_id)
        },
        {
            "$set": tab_data
        }
    )

    if updated.modified_count == 1:
        new_tab = await tab_collection.find_one({"_id": ObjectId(tab_id)})
        return {
            "id": str(new_tab["_id"]),
            "title": new_tab["title"],
            "artist": new_tab["artist"],
            "content": new_tab["content"],
        }

    return None

async def delete_tab(tab_id:str) -> bool:
    if not ObjectId.is_valid(tab_id):
        return False
    delete_result = await tab_collection.delete_one(
        {"_id": ObjectId(tab_id)}
    )

    return delete_result.deleted_count == 1
