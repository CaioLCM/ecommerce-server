from fastapi import APIRouter, FastAPI

user_router = APIRouter()

@user_router.get("/login")
def handle_login():
    print("--- login logic ---")
    
@user_router.post("/register")
def handle_register():
    print("--- register logic ---")
    
@user_router.put("/update")
def handle_update():
    print("--- update logic ---")
    

    