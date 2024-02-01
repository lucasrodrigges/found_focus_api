from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.user_schemas import CreateUserSchema
from src.database.init import get_session
from src.services.users.find_user_by_unique import find_user_by_unique


def user_already_exists(
    user: CreateUserSchema,
    session: Session = Depends(get_session),
):
    found_user = find_user_by_unique(user, session)
    if found_user:
        raise HTTPException(
            status_code=400,
            detail="User already registered",
        )
