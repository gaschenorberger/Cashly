from db.config import conn

def registerUserDb(nome, email, senha):
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

            usuario_id = cursor.fetchone()[0]
            conn.commit()

            return {
                "status": "OK",
                "mensagem": "Usuário cadastrado",
                "usuario_id": usuario_id
            }

    except Exception as e:
        conn.rollback()

        return {
            "status": "ERROR",
            "mensagem": "Erro ao cadastrar usuário",
            "erro": str(e)
        }