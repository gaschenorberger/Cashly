from pydantic import BaseModel

class RegisterUser(BaseModel):
    nome: str
    email: str
    senha: str

class LoginUser(BaseModel):
    email: str
    senha: str