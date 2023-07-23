from pydantic import BaseModel, EmailStr, UserSchema

class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int
