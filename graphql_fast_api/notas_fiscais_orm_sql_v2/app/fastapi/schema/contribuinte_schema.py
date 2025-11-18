from typing import List, Optional
from pydantic import BaseModel
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
    danfes: List[Danfe] = []
    enderecos: List[Endereco] = []

    class Config:
        from_attributes = True


class Response(BaseModel):
    data: Contribuinte


class PaginatedResponse(BaseModel):
    page: int
    page_size: int
    data: List[Contribuinte]
