from typing_extensions import Annotated
from pydantic import AfterValidator, Field


def _cd_contribuinte_only_digits(v: str):
    if v is None:
        return None

    if not v.isdigit():
        raise ValueError("cd_contribuinte deve conter apenas números")

    return v


def _cnpj_contribuinte_only_digits(v: str):
    if v is None:
        return None

    if not v.isdigit():
        raise ValueError("cnpj_contribuinte deve conter apenas números")

    return v


CdContribuinte = Annotated[
    str,
    Field(min_length=9, max_length=20),
    AfterValidator(_cd_contribuinte_only_digits)
]


CnpjContribuinte = Annotated[
    str,
    Field(min_length=14, max_length=14),
    AfterValidator(_cnpj_contribuinte_only_digits)
]
