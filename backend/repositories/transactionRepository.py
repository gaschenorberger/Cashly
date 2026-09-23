from backend.BaseModels.transactions.transactionModel import NewTransaction
from db.config import getConn, putConn

def setNewTransaction(userId, transaction: NewTransaction):
    conn = getConn()

    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO transacoes (usuario_id_fk, categoria_id_fk, nome_transacao, valor, tipo_transacao, data_transacao, observacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    userId,
                    transaction.categoriaId,
                    transaction.nomeTransacao,
                    transaction.valor,
                    transaction.tipoTransacao.value,
                    transaction.dataTransacao,
                    transaction.observacao
                )
            )

            transacaoId = cursor.fetchone()[0]
            conn.commit()

            return {
                "status": "OK",
                "mensagem": "Transação cadastrada",
                "transacao_id": transacaoId
            }
    except Exception:
        conn.rollback()
        raise 
    finally:
        putConn(conn)