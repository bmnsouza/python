from enum import Enum

from typing import Optional

import strawberry


@strawberry.input
class ContribuinteFiltersInput:
    cd_contribuinte: Optional[str] = None
    cnpj_contribuinte: Optional[str] = None
    nm_fantasia: Optional[str] = None


@strawberry.enum
class OrderDirection(Enum):
    ASC = "asc"
    DES = "des"


@strawberry.input
class OrderInput:
    field: str
    direction: OrderDirection = OrderDirection.ASC
