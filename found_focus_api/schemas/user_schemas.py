from pydantic import BaseModel, EmailStr


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserListPublic(BaseModel):
    users: list[UserPublic]


class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
