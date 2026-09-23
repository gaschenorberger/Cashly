from fastapi import APIRouter, Depends, status
from backend.BaseModels.transactions.transactionModel import NewTransaction
from backend.security.security import getCurrentUserId
from backend.service.transactions import transactionService

transaction_router = APIRouter(prefix="/transaction", tags=["Transações"])

@transaction_router.post("/newTransaction", status_code=status.HTTP_201_CREATED)
async def newTransaction(transaction: NewTransaction, userId: int = Depends(getCurrentUserId)):
   return transactionService.createNewTransaction(userId, transaction)