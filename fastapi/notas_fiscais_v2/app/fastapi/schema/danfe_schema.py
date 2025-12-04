from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class DanfeBase(BaseModel):
    cd_contribuinte: Optional[str] = None
    numero: Optional[str] = None
    valor_total: Optional[Decimal] = None
    data_emissao: Optional[datetime] = None
    class Config:
        from_attributes = True


class Danfe(DanfeBase):
    id_danfe: Optional[int] = None
    class Config:
        from_attributes = True


class DanfeCreate(BaseModel):
    cd_contribuinte: str
    numero: str
    valor_total: Decimal
    data_emissao: datetime


class DanfeUpdate(BaseModel):
    numero: str
    valor_total: Decimal
    data_emissao: datetime
