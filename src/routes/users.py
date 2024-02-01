from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.schemas.user_schemas import CreateUserSchema, UserPublic
from src.database.init import get_session
from src.services.users.create_user import create_user


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=201, response_model=UserPublic)
def create_user_controller(
    user: CreateUserSchema,
    session: Session = Depends(get_session),
):
    created_user = create_user(user, session)
    return created_user
