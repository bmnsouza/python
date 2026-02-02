from datetime import date
from decimal import Decimal

import strawberry

from app.presentation.graphql.inputs.order_input import OrderDirection

@strawberry.input
class DanfeFilterInput:
    cd_contribuinte: str | None = None
    numero: str | None = None
    valor_total: Decimal | None = None
    data_emissao: date | None = None


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
    cd_contribuinte: OrderDirection | None = None
    cnpj_contribuinte: OrderDirection | None = None
    nm_fantasia: OrderDirection | None = None
