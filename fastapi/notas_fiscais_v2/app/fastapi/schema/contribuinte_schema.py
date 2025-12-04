from typing import List, Optional
from pydantic import BaseModel

from app.fastapi.schema.danfe_schema import Danfe
from app.fastapi.schema.endereco_schema import Endereco


class ContribuinteBase(BaseModel):
    cd_contribuinte: Optional[str] = None
    cnpj_contribuinte: Optional[str] = None
    nm_fantasia: Optional[str] = None
    class Config:
        from_attributes = True


class Contribuinte(ContribuinteBase):
    danfes: Optional[List[Danfe]] = None
    enderecos: Optional[List[Endereco]] = None
    class Config:
        from_attributes = True


class ContribuinteCreate(BaseModel):
    cd_contribuinte: str
    cnpj_contribuinte: str
    nm_fantasia: str


class ContribuinteUpdate(BaseModel):
    cnpj_contribuinte: str
    nm_fantasia: str
