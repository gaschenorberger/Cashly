from db.config import conn


def getByEmail(email: str):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, nome, email, senha_hash
                FROM usuarios
                WHERE email = %s
                """,
                (email,)
            )
            return cursor.fetchone()
    except Exception:
        conn.rollback()
        raise


def setNewUser(nome, email, senha):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO usuarios (nome, email, senha_hash)
                VALUES (%s, %s, %s)
                RETURNING id
                """,
                (nome, email, senha)
            )

            usuarioId = cursor.fetchone()[0]
            conn.commit()

            return {
                "status": "OK",
                "mensagem": "Usuário cadastrado",
                "usuario_id": usuarioId
            }

    except Exception as e:
        conn.rollback()

        return {
            "status": "ERROR",
            "mensagem": "Erro ao cadastrar usuário",
            "erro": str(e)
        }

def getUserAtivo(email):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT ativo
                FROM usuarios
                WHERE email = %s
                """,
                (email,)
            )

            usuarioAtivo = cursor.fetchone()[0]
            return usuarioAtivo
    except Exception:
        conn.rollback()
        raise

def setUserInativo(email):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                UPDATE usuarios
                SET ativo = FALSE
                WHERE email = %s
                """,
                (email,)
            )
            conn.commit()
    except Exception:
        conn.rollback()
        raise