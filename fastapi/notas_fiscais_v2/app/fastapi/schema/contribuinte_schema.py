from typing import List, Optional
from pydantic import BaseModel

from app.fastapi.schema.danfe_schema import Danfe
from app.fastapi.schema.endereco_schema import Endereco
from app.fastapi.validators.contribuinte_validators import CD_CONTRIBUINTE_PATH, CNPJ_CONTRIBUINTE_PATH, NM_FANTASIA_PATH


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
    cd_contribuinte: str = CD_CONTRIBUINTE_PATH
    cnpj_contribuinte: str = CNPJ_CONTRIBUINTE_PATH
    nm_fantasia: str = NM_FANTASIA_PATH


class ContribuinteUpdate(BaseModel):
    cnpj_contribuinte: str = CNPJ_CONTRIBUINTE_PATH
    nm_fantasia: str = NM_FANTASIA_PATH
