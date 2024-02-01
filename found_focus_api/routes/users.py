from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from found_focus_api.schemas.user_schemas import (
    CreateUserSchema,
    UserPublic,
    UserListPublic,
)
from found_focus_api.database.init import get_session
from found_focus_api.services.users.create_user import create_user
from found_focus_api.services.users.read_users import read_users


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=200, response_model=UserListPublic)
def read_users_controller(session: Session = Depends(get_session)):
    users = read_users(session)
    return {"users": users}


@router.post("/", status_code=201, response_model=UserPublic)
def create_user_controller(
    user: CreateUserSchema, session: Session = Depends(get_session)
):
    created_user = create_user(user, session)
    return created_user
