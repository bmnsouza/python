from datetime import date
from decimal import Decimal
from typing import Optional

import strawberry


@strawberry.input
class DanfeParamsInput:
    cd_contribuinte: Optional[str] = None
    numero: Optional[str] = None
    valor_total: Optional[Decimal] = None
    data_emissao: Optional[date] = None


@strawberry.input
class DanfeParamInput:
    id_danfe: int
