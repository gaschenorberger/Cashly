from db.config import getConn, putConn

def setNewCategory(userId, nomeCategoria):
    conn = getConn()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO categorias (usuario_id_fk, nome_categoria)
                VALUES (%s, %s)
                RETURNING id
                """,
                (userId, nomeCategoria)
            )

            categoriaId = cursor.fetchone()[0]
            conn.commit()

            return {
                "status": "OK",
                "mensagem": "Categoria cadastrada",
                "categoria_id": categoriaId
            }
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        putConn(conn)