import json
from datetime import datetime

from pydantic import BaseModel, field_validator


class DanfeItemDTO(BaseModel):
    numero: str | None
    valor_total: float | None
    data_emissao: datetime | None


class DanfeDTO(BaseModel):
    cnpj_contribuinte: str | None
    nm_fantasia: str | None
    logradouro: str | None
    municipio: str | None
    uf: str | None
    danfe: list[DanfeItemDTO] | None

    @field_validator("danfe", mode="before")
    @classmethod
    def parse_danfe_json(cls, value):
        if value is None:
            return []

        if isinstance(value, str):
            return json.loads(value)

        return value
