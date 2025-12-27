from typing import List, Optional
from pydantic import BaseModel, Field

from app.schema.danfe_schema import Danfe
from app.schema.endereco_schema import Endereco


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


class ContribuinteUpdate(BaseModel):
    cnpj_contribuinte: Optional[str] = Field(default=None, min_length=14, max_length=14)
    nm_fantasia: Optional[str] = Field(default=None, min_length=5, max_length=200)


class ContribuinteCreate(BaseModel):
    cd_contribuinte: str = Field(min_length=9, max_length=20)
    cnpj_contribuinte: str = Field(min_length=14, max_length=14)
    nm_fantasia: str = Field(min_length=5, max_length=200)


class ContribuinteItem(BaseModel):
    cd_contribuinte: str
    cnpj_contribuinte: str
    nm_fantasia: str
