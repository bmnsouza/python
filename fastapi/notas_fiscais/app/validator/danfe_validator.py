from datetime import date
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field


class DanfeParams(BaseModel):
    cd_contribuinte: Optional[str] = Field(default=None, min_length=9, max_length=20)
    numero: Optional[str] = Field(default=None, min_length=5, max_length=15)
    valor_total: Optional[Decimal] = Field(default=None, max_digits=12, decimal_places=2)
    data_emissao: Optional[date] = Field(default=None)


class DanfeParam(BaseModel):
    id_danfe: int = Field(..., ge=1, le=9_999_999_999)


class DanfeLastSevenDaysParam(BaseModel):
    cd_contribuinte: str = Field(..., min_length=9, max_length=20)
