from fastapi import APIRouter, HTTPException


from backend.BaseModels.auth.authModel import RegisterUser, LoginUser
from backend.service.auth import authService

auth_router = APIRouter(prefix="/auth/v1", tags=["Authentication"])


@auth_router.post("/register", status_code=201)
async def registerUser(user: RegisterUser):
    return authService.register(user.nome, user.email, user.senha)


@auth_router.post("/login", status_code=200)
def login(user: LoginUser):
    return authService.login(user.email, user.senha)

