from datetime import datetime

from pydantic import BaseModel


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
