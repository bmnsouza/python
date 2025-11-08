from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

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
        orm_mode = True
