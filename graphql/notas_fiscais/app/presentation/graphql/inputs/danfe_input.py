from datetime import date
from decimal import Decimal

import strawberry

from app.presentation.graphql.inputs.order_input import OrderDirection

@strawberry.input
class DanfeListFilterInput:
    cd_contribuinte: str | None = None
    numero: str | None = None
    valor_total: Decimal | None = None
    data_emissao: date | None = None


@strawberry.input
class DanfeListOrderInput:
    cd_contribuinte: OrderDirection | None = None
    cnpj_contribuinte: OrderDirection | None = None
    nm_fantasia: OrderDirection | None = None


@strawberry.input
class DanfeLastSevenDaysFilterInput:
    cd_contribuinte: str


@strawberry.input
class DanfeMonthlyFilterInput:
    cd_contribuinte: str
    year: int
    month: int
