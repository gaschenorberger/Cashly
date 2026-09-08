from fastapi import HTTPException

from backend.repositories import userRepository
from backend.security import security


def login(email: str, senha: str):
    try:
        usuario = userRepository.getByEmail(email)

        if not usuario:
            raise HTTPException(status_code=400, detail="Email ou senha invalidos")

        senhaHash = usuario[3]

        if not security.verify_password(senha, senhaHash):
            raise HTTPException(status_code=400, detail="Email ou senha invalidos")


        token = security.create_access_token({"sub": str(usuario.id)})

        return {
            "status": "OK",
            "mensagem": "Login efetuado",
            "access_token": token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "mensagem": "Erro interno ao efetuar login",
                "detalhes do erro": str(e)
            }
        )


def register(nome, email, senha):
    try:
        senhaHash = security.hash_password(senha)
        registerUser = userRepository.setNewUser(nome, email, senhaHash)

        if registerUser["status"] != "OK":
            raise HTTPException(
                status_code=400,
                detail={
                    "Status": "error",
                    "Mensagem": "Erro ao cadastrar usuario",
                },
            )

        return {
            "Status": "accepted",
            "Mensagem": "Usuario cadastrado",
            "Data": {
                "ID": registerUser["usuario_id"],
                "Nome": nome,
                "Email": email,
            },
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "Status": "error",
                "Mensagem": "Erro interno ao cadastrar usuario",
                "Detalhes do erro": str(e),
            },
        )
