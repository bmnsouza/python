from typing import Annotated

from fastapi import Path
from pydantic import Field


ID_ENDERECO_PATH = Annotated[
    int,
    Path(
        max_digits=10,
        description="ID Endereço deve conter no máximo 10 dígitos"
    )
]

LOGRADOURO_FIELD = Field(
    ...,
    min_length=14,
    max_length=14,
    description="CNPJ do contribuinte deve conter 14 caracteres"
)

MUNICIPIO_FIELD = Field(
    ...,
    min_length=3,
    max_length=200,
    description="Nome Fantasia deve conter no mínimo 3 e no máximo 200 caracteres"
)

UF_FIELD = Field(
    ...,
    min_length=14,
    max_length=14,
    description="CNPJ do contribuinte deve conter 14 caracteres"
)
