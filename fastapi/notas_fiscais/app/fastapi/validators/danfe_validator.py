from datetime import date
from decimal import Decimal
from typing import Annotated

from fastapi import Path
from pydantic import Field


ID_DANFE_PATH = Annotated[
    int,
    Path(
        max_digits=10,
        description="ID Danfe deve conter no máximo 10 dígitos"
    )
]

NUMERO_FIELD = Field(
    ...,
    min_length=5,
    max_length=25,
    description="Número do DANFE deve conter no mínimo 5 caracteres e no máximo 25"
)

VALOR_TOTAL_FIELD = Annotated[
    Decimal,
    Field(
        max_digits=12,
        decimal_places=2,
        description="Valor total deve conter no máximo 12 dígitos, sendo 10 inteiros e 2 decimais"
    )
]

DATA_EMISSAO_FIELD = Annotated[
    date,
    Field(
        description="Data e hora da emissão no formato YYYY-MM-DD"
    )
]
