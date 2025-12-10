from fastapi import Path
from pydantic import Field


MIN_LENGTH_CD_CONTRIBUINTE = 9
MAX_LENGTH_CD_CONTRIBUINTE = 20
DESCRIPTION_CD_CONTRIBUINTE = f"Código do contribuinte deve ter no mínimo {MIN_LENGTH_CD_CONTRIBUINTE} e no máximo {MAX_LENGTH_CD_CONTRIBUINTE} caracteres"

CD_CONTRIBUINTE_PATH = Path(
    ...,
    min_length=MIN_LENGTH_CD_CONTRIBUINTE,
    max_length=MAX_LENGTH_CD_CONTRIBUINTE,
    description=DESCRIPTION_CD_CONTRIBUINTE
)

CD_CONTRIBUINTE_FIELD = Field(
    ...,
    min_length=MIN_LENGTH_CD_CONTRIBUINTE,
    max_length=MAX_LENGTH_CD_CONTRIBUINTE,
    description=DESCRIPTION_CD_CONTRIBUINTE
)

CNPJ_CONTRIBUINTE_FIELD = Field(
    ...,
    min_length=14,
    max_length=14,
    description="CNPJ do contribuinte deve ter 14 caracteres"
)

NM_FANTASIA_FIELD = Field(
    ...,
    min_length=5,
    max_length=200,
    description="Nome Fantasia deve ter no mínimo 5 e no máximo 200 caracteres"
)
