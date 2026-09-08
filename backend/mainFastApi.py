"""
uvicorn backend.mainFastApi:app --reload --port 8001
"""

from fastapi import FastAPI
from backend.controller.auth.authController import auth_router
from backend.controller.transactions.transactionController import transaction_router

app = FastAPI()

@app.get("/")
def health():
    return {"API": "Running"}

app.include_router(auth_router)
app.include_router(transaction_router)
