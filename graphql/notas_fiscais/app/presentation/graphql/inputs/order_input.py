from enum import Enum

import strawberry


@strawberry.enum
class OrderDirection(Enum):
    ASC = "asc"
    DESC = "desc"
