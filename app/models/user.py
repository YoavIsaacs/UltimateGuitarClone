from pydantic import BaseModel
from passlib.context import CryptContext


class UserCreate(BaseModel):
    username: str
    password: str

class UserInDb(UserCreate):
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)