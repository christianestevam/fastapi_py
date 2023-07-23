from fastapi_py.schemas import UserSchema, UserPublic, UserDB



database = []  


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return UserPublic(**user_with_id.model_dump())