from datetime import date
from decimal import Decimal
from typing import Optional

import strawberry

from app.presentation.graphql.inputs.order_input import OrderDirection

@strawberry.input
class DanfeFilterInput:
    cd_contribuinte: Optional[str] = None
    numero: Optional[str] = None
    valor_total: Optional[Decimal] = None
    data_emissao: Optional[date] = None


@strawberry.input
class DanfeFilterLastSevenDaysInput:
    cd_contribuinte: str


@strawberry.input
class DanfeFilterMonthlyInput:
    cd_contribuinte: str
    year: int
    month: int


@strawberry.input
class DanfeOrderInput:
    cd_contribuinte: Optional[OrderDirection] = None
    cnpj_contribuinte: Optional[OrderDirection] = None
    nm_fantasia: Optional[OrderDirection] = None
