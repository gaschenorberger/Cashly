from db.config import getConn, putConn


def getByEmail(email: str):
    conn = getConn()

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
    finally:
        putConn(conn)

def setNewUser(nome, email, senha):
    conn = getConn()
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
    finally:
        putConn(conn)

def getUserAtivo(email): # O usuário esta ativo ou inativo? (True/False)
    conn = getConn()

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
    finally:
        putConn(conn)

def setUserInativo(email):
    conn = getConn()

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
    finally:
        putConn(conn)