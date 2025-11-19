from typing import List, Optional
from pydantic import BaseModel, Field
from .danfe_schema import Danfe
from .endereco_schema import Endereco


class ContribuinteBase(BaseModel):
    cd_contribuinte: str
    nm_fantasia: Optional[str] = None
    cnpj_contribuinte: Optional[str] = None


class ContribuinteCreate(ContribuinteBase):
    pass


class ContribuinteUpdate(BaseModel):
    nm_fantasia: Optional[str] = None
    cnpj_contribuinte: Optional[str] = None


class Contribuinte(ContribuinteBase):
    danfes:  List[Danfe] = Field(default_factory=list)
    enderecos:  List[Endereco] = Field(default_factory=list)
    class Config:
        from_attributes = True


class SingleResponse(BaseModel):
    data: Contribuinte


class PaginatedResponse(BaseModel):
    page: int
    page_size: int
    data: List[Contribuinte]
