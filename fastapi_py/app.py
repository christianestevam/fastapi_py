from fastapi import FastAPI
emafrom fastapi_py.schemas import UserSchema

# Código da nossa rota de olá mundo omitido

@app.post('/users/', status_code=201)
def create_user(user: UserSchema):
    return user