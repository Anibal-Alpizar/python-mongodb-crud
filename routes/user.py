from fastapi import APIRouter
from config.db import conn
from schemas.user import usersEntity, userEntity
from models.user import User

router = APIRouter()

@router.get("/users" )
def find_all_users():
    return usersEntity(conn.local.user.find())

@router.post("/users")
def create_user(user: User):
    new_user = dict(user)
    del new_user['id'] # remove id field from the document
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)