from pydantic import BaseModel
from passlib.context import CryptContext


class UserCreate(BaseModel):
    username: str
    password: str

class UserInDb(UserCreate):
    hashed_password: str
