from db.config import conn

def loginUserDb(email, senha):
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT status_execucao FROM tbl_status_execucao
                """, 
            )
            resultado = cursor.fetchone()

        return resultado
    except Exception as e:
        conn.rollback()   
        print("Erro ao obter status:", e)