from typing import List, Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class DanfeBase(BaseModel):
    cd_contribuinte: str
    numero: Optional[str] = None
    valor_total: Optional[Decimal] = None
    data_emissao: Optional[datetime] = None


class DanfeCreate(DanfeBase):
    pass


class DanfeUpdate(BaseModel):
    numero: Optional[str] = None
    valor_total: Optional[Decimal] = None
    data_emissao: Optional[datetime] = None

class Danfe(DanfeBase):
    id_danfe: int
    class Config:
        from_attributes = True


class DanfeFiltro(BaseModel):
    cd_contribuinte: Optional[str] = None
    numero: Optional[str] = None
    valor_minimo: Optional[float] = None
    valor_maximo: Optional[float] = None
    data_inicial: Optional[datetime] = None
    data_final: Optional[datetime] = None


class SingleResponse(BaseModel):
    data: Danfe


class PaginatedResponse(BaseModel):
    page: int
    page_size: int
    data: List[Danfe]
