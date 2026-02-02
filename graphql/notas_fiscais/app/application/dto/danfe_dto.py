from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class DanfeListDTO(BaseModel):
    id_danfe: int
    cd_contribuinte: str
    numero: str
    valor_total: Decimal
    data_emissao: datetime


class DanfeLastSevenDaysDTO(BaseModel):
    cd_contribuinte: str
    numero: str
    valor_total: Decimal
    data_emissao: datetime


class DanfeMonthlyDTO(BaseModel):
    numero: str
    valor_total: Decimal
    data_emissao: datetime
