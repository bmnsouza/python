from pydantic import BaseModel


class ContribuinteDTO(BaseModel):
    cd_contribuinte: str
    cnpj_contribuinte: str
    nm_fantasia: str
