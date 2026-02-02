from pydantic import BaseModel


class ContribuinteListDTO(BaseModel):
    cd_contribuinte: str
    cnpj_contribuinte: str
    nm_fantasia: str
