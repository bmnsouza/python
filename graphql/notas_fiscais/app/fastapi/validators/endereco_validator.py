from typing import Annotated

from fastapi import Path
from pydantic import Field


ID_ENDERECO_PATH = Annotated[
    int,
    Path(
        max_digits=10,
        description="ID Endereço deve ter no máximo 10 dígitos"
    )
]

LOGRADOURO_FIELD = Field(
    ...,
    min_length=5,
    max_length=200,
    description="Logradouro deve ter no mínimo 5 e no máximo 200 caracteres"
)

MUNICIPIO_FIELD = Field(
    ...,
    min_length=5,
    max_length=100,
    description="Município deve ter no mínimo 5 e no máximo 100 caracteres"
)

UF_FIELD = Field(
    ...,
    min_length=2,
    max_length=2,
    description="UF deve ter 2 caracteres"
)
