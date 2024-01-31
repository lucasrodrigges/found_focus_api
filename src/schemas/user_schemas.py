from pydantic import BaseModel, EmailStr


class UserPublic(BaseModel):
    name: str
    email: EmailStr


class CreateUserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
