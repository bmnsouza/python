from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel


class ContribuinteDanfeMonthlyDTO(BaseModel):
    cd_contribuinte: str
    cnpj_contribuinte: str
    nm_fantasia: str
    numero: str
    valor_total: Decimal
    data_emissao: datetime
