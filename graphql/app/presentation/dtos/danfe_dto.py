from datetime import datetime

from pydantic import BaseModel


class DanfeDTO(BaseModel):
    cnpj_contribuinte: str | None
    nm_fantasia: str | None
    numero: str | None
    valor_total: float | None
    data_emissao: datetime | None
    logradouro: str | None
    municipio: str | None
    uf: str | None
