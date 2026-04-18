from pydantic import BaseModel


class ContribuinteDTO(BaseModel):
    cnpj_contribuinte: str | None
    nm_fantasia: str | None
