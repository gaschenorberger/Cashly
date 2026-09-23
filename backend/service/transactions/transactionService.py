from fastapi import HTTPException, status

from backend.BaseModels.transactions.transactionModel import NewTransaction
from backend.repositories import transactionRepository


def createNewTransaction(userId, transaction: NewTransaction):
    try:    
        newTransaction =  transactionRepository.setNewTransaction(userId, transaction)

        return {
            "Status": "accepted",
            "Mensagem": "Nova transação cadastrada",
            "data": {
                "ID da transação": newTransaction["transacao_id"],
                "Nome da transação": transaction.nomeTransacao,
                "Valor da transação": transaction.valor,   
                "Tipo da transação": transaction.tipoTransacao,
                "Categoria da transação": transaction.categoriaId,
                "Data da transação": transaction.dataTransacao,
                "Observação": transaction.observacao
            }
        }
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro interno ao cadastrar transação")