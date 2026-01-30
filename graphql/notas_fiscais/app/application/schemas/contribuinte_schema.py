from pydantic import BaseModel


class Contribuinte(BaseModel):
    cd_contribuinte: str
    cnpj_contribuinte: str
    nm_fantasia: str
