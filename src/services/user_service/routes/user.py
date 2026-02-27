from fastapi import APIRouter, Response
from ..database import login, register
from pydantic import BaseModel

user_router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@user_router.post("/login")
def handle_login(user: User):
    response = login(username=user.username, password=user.password)
    if response:
        return {"message": "success!"}
    else:
        return {"message": "error!"}
    
@user_router.post("/register")
def handle_register(user: User):
    register(username=user.username, password=user.password)
    
@user_router.put("/update")
def handle_update():
    print("--- update logic ---")
    

    