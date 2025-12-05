from fastapi import Path


CD_CONTRIBUINTE_PATH = Path(
    ...,
    min_length=9,
    max_length=20,
    description="Código do contribuinte deve conter no mínimo 9 e no máximo 20 caracteres"
)

CNPJ_CONTRIBUINTE_PATH = Path(
    ...,
    min_length=14,
    max_length=14,
    description="CNPJ do contribuinte deve conter 14 caracteres"
)

NM_FANTASIA_PATH = Path(
    ...,
    min_length=3,
    max_length=200,
    description="Nome Fantasia deve conter no mínimo 3 e no máximo 200 caracteres"
)
