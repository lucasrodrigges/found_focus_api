from fastapi import Depends
from sqlalchemy.orm import Session

from found_focus_api.schemas.user_schemas import CreateUserSchema
from found_focus_api.database.init import get_session
from found_focus_api.services.users.user_already_exists import user_already_exists
from found_focus_api.models.main import User


def create_user(
    user: CreateUserSchema,
    session: Session = Depends(get_session),
):
    # Check if user already exists and raise an exception if it does
    user_already_exists(user, session)

    # Create a new user
    db_user = User(
        name=user.name,
        email=user.email,
        password=user.password,
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user
