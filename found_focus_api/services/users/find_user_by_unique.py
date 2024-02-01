from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from src.schemas.user_schemas import CreateUserSchema
from src.database.init import get_session
from src.models.main import User


def find_user_by_unique(
    user: CreateUserSchema,
    session: Session = Depends(get_session),
):
    found_user = session.scalar(
        select(User).where(
            User.email == user.email,
        ),
    )
    return found_user
