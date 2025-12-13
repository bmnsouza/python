from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel

from app.fastapi.validators.contribuinte_validator import CD_CONTRIBUINTE_FIELD
from app.fastapi.validators.danfe_validator import NUMERO_FIELD, VALOR_TOTAL_FIELD, DATA_EMISSAO_FIELD


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
    numero: str = NUMERO_FIELD
    valor_total: Decimal = VALOR_TOTAL_FIELD
    data_emissao: datetime = DATA_EMISSAO_FIELD


class DanfeCreate(DanfeUpdate):
    cd_contribuinte: str = CD_CONTRIBUINTE_FIELD
