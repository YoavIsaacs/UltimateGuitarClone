from fastapi import APIRouter, HTTPException, status
from app.models.user import UserCreate, UserInDb
from app.databaseConnection import database
from app.utils import get_password_hash, verify_password, create_access_token

router = APIRouter()
user_collection = database.get_collection("users")

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
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

@router.post("/login")
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









