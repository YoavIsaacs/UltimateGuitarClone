from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends

from app.core.dependencies import get_current_user
from app.models.user import UserCreate, UserInDb
from app.databaseConnection import database
from app.utils import get_password_hash, verify_password, create_access_token

auth_router = APIRouter()
user_collection = database.get_collection("users")

@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    print("hello")
    existing_user = await user_collection.find_one(
        {"username": user.username}
    )

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(user.password)

    user_in_db = UserInDb(
        username=user.username,
        hashed_password=hashed_password
    )

    await user_collection.insert_one(user_in_db.model_dump())

    return {
        "message": "User created successfully"
    }

@auth_router.post("/login")
async def login_user(user: UserCreate):
    existing_user = await user_collection.find_one(
        {"username": user.username}
    )

    if not existing_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    if not verify_password(user.password, existing_user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token = create_access_token(data={"sub": user.username})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@auth_router.get("/get_all_users")
async def get_all_users():
    users_cursor = user_collection.find()  # This returns a cursor
    users = await users_cursor.to_list(length=None)  # Convert the cursor to a list

    # Convert ObjectId to string for each user
    for user in users:
        if '_id' in user:
            user['_id'] = str(user['_id'])

    return users



