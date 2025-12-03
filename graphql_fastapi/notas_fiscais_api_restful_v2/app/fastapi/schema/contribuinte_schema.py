# app/fastapi/schema/contribuinte_schema.py
from typing import List, Optional
from pydantic import BaseModel, Field

from app.fastapi.schema.danfe_schema import Danfe
from app.fastapi.schema.endereco_schema import Endereco


class ContribuinteBase(BaseModel):
    cd_contribuinte: str
    cnpj_contribuinte: Optional[str] = None
    nm_fantasia: Optional[str] = None


class ContribuinteCreate(ContribuinteBase):
    pass


class ContribuinteUpdate(BaseModel):
    cnpj_contribuinte: Optional[str] = None
    nm_fantasia: Optional[str] = None


class Contribuinte(ContribuinteBase):
    danfes: List[Danfe] = Field(default_factory=list)
    enderecos: List[Endereco] = Field(default_factory=list)

    class Config:
        from_attributes = True


class SingleResponse(BaseModel):
    data: Contribuinte


class PaginatedOffsetResponse(BaseModel):
    offset: int
    limit: int
    total: int
    data: List[Contribuinte]
