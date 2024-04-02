from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oAuth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "osorio": {
        "username": "osorio",
        "full_name": "David Osorio",
        "email": "david.lml.95@gmail.com",
        "password": "123456",
        "disabled": False
    }
}

def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])

async def current_user(token: str = Depends(oAuth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=401, detail="No autorizado", headers={"WWW-Authenticate": "bearer"})
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    user = search_user(form.username)
    if not user.password == form.password:
        raise HTTPException(status_code=400, detail="La contraseñ no es correcta")

    return {"acces_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user