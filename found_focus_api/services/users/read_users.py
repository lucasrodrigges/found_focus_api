from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import select

from found_focus_api.database.init import get_session
from found_focus_api.models.main import User


def read_users(session: Session = Depends(get_session)):
    users = session.scalars(select(User)).all()
    return users
