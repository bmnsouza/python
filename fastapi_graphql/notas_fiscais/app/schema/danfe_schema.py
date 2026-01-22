from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field


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


class DanfeUpdate(BaseModel):
    numero: Optional[str] = Field(default=None, min_length=5, max_length=15)
    valor_total: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=2)
    data_emissao: Optional[datetime] = Field(default=None)


class DanfeCreate(BaseModel):
    cd_contribuinte: str = Field(..., min_length=9, max_length=20)
    numero: str = Field(..., min_length=5, max_length=15)
    valor_total: Decimal = Field(..., max_digits=12, decimal_places=2)
    data_emissao: datetime = Field(...)


class DanfeItem(BaseModel):
    id_danfe: int
    cd_contribuinte: str
    numero: str
    valor_total: Decimal
    data_emissao: datetime


class DanfeLastSevenDaysItem(BaseModel):
    cd_contribuinte: str
    numero: str
    valor_total: Decimal
    data_emissao: datetime
