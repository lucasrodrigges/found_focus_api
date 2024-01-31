from fastapi import APIRouter
from src.schemas.user_schemas import CreateUserSchema, UserPublic


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=201, response_model=UserPublic)
def create_user(user: CreateUserSchema):
    return user
