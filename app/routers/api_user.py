from fastapi import APIRouter, Form
from app.services.user_storage import load_users, create_user

router = APIRouter()

@router.post("/api/user/new")
def new_user(
    name: str=Form(), 
    permission: str=Form("user"),
    company: str=Form(),
    email: str=Form(),
    password: str=Form(),
    username: str=Form()
):
    user = create_user(name, permission, company, email, password, username)

    return {"Created": user}