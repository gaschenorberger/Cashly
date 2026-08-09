from fastapi import APIRouter, HTTPException
from pwdlib import PasswordHash

from backend.BaseModels.auth.authModel import RegisterUser, LoginUser
from backend.service.auth.registerUserDb import registerUserDb

auth_router = APIRouter(prefix="/auth/v1", tags=["Authentication"])
password_hash = PasswordHash.recommended()


def gerarHashSenha(senha: str) -> str:
    return password_hash.hash(senha)

@auth_router.post("/register")
async def registerUser(user: RegisterUser):
    try:
        nomeUsuario = user.nome
        emailUsuario = user.email
        senhaHash = gerarHashSenha(user.senha)

        result = registerUserDb(nomeUsuario, emailUsuario, senhaHash)

        if result["status"] != "OK":
            raise HTTPException(
                status_code=400,
                detail={
                    "Status": "error",
                    "Mensagem": "Erro ao cadastrar usuário",
                    "Detalhes do erro": result["erro"]
                }
            )

        return {
            "Status": "accepted",
            "Mensagem": "Usuário cadastrado",
            "Data": {
                "Nome": nomeUsuario,
                "Email": emailUsuario
            }
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "Status": "error",
                "Mensagem": "Erro interno ao cadastrar usuário",
                "Detalhes do erro": str(e)
            }
        )

@auth_router.post("/login")
async def loginUser(user: LoginUser):
    try:
        emailUsuario = user.email
        cpfUsuario = user.cpf
        senhaUsuario = user.senha

        return {
            "Status": "accepted",
            "Mensagem": "Login Efetuado",
            "Data": {
                "Email": emailUsuario,
                "Cpf": cpfUsuario,
                "Senha": senhaUsuario
            },
        }
    except Exception as e:
        return {
            "Status": "error",
            "Mensagem": "Erro ao efetuar login",
            "Detalhes do erro": str(e)
        }


