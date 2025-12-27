from enum import Enum

import strawberry


@strawberry.enum
class OrderDirection(Enum):
    ASC = "asc"
    DES = "des"


@strawberry.input
class OrderInput:
    field: str
    direction: OrderDirection = OrderDirection.ASC
