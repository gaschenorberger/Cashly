from datetime import date
from pydantic import BaseModel, Field
from enum import Enum
from decimal import Decimal

class TransactionType(str, Enum):
    entrada = "entrada"
    saida = "saida"

class CategoryType(str, Enum):
    alimentacao = "alimentação"
    transporte = "transporte"
    saude = "saúde"
    educacao = "educação"
    lazer = "lazer"
    salario = "salário"
    outros = "outros"

class NewTransaction(BaseModel):
    nomeTransacao: str
    valor: Decimal = Field(gt=0, decimal_places=2)
    tipoTransacao: TransactionType
    categoria: CategoryType
    dataTransacao: date
    observacao: str | None = None
