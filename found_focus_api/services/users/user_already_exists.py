from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from found_focus_api.schemas.user_schemas import CreateUserSchema
from found_focus_api.database.init import get_session
from found_focus_api.services.users.find_user_by_unique import find_user_by_unique


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
