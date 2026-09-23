from datetime import date
from pydantic import BaseModel, Field
from enum import Enum
from decimal import Decimal

class TransactionType(str, Enum):
    entrada = "entrada"
    saida = "saida"

class NewTransaction(BaseModel):
    nomeTransacao: str = Field(min_length=1, max_length=255)
    valor: Decimal = Field(gt=0, max_digits=12, decimal_places=2)
    tipoTransacao: TransactionType
    categoriaId: int = Field(gt=0)
    dataTransacao: date
    observacao: str | None = None