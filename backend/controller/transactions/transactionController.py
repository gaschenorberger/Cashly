from fastapi import APIRouter, Depends
from backend.BaseModels.transactions.transactionModel import NewTransaction
from backend.security.security import getCurrentUserId

transaction_router = APIRouter(prefix="/transaction", tags=["Transações"])

@transaction_router.post("/newTransaction")
async def newTransaction(transaction: NewTransaction, userId: int = Depends(getCurrentUserId)):
    try:
        nomeTransacao = transaction.nomeTransacao
        valorTransacao = transaction.valor
        tipoTransacao = transaction.tipoTransacao
        categoriaTransacao = transaction.categoria
        dataTransacao = transaction.dataTransacao
        observacao = transaction.observacao

        return {
            "Status": "accepted",
            "Mensagem": "Nova transação cadastrada",
            "Nome da transação": nomeTransacao,
            "Valor da transação": valorTransacao,   
            "Tipo da transação": tipoTransacao,
            "Categoria da transação": categoriaTransacao,
            "Data da transação": dataTransacao,
            "Observação": observacao
        }
    except Exception as e:
        return {
            "Status": "error",
            "Mensagem": "Erro ao cadastrar transação",
            "Detalhes do erro": str(e)
        }