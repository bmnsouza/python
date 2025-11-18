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


class SingleResponse(BaseModel):
    data: Danfe


class PaginatedResponse(BaseModel):
    page: int
    page_size: int
    data: List[Danfe]
