from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.danfe_dto import DanfeDTO, DanfeLastSevenDaysDTO, DanfeMonthlyDTO


@pydantic_type(model=DanfeDTO, all_fields=True)
class DanfeType:
    pass


@strawberry.type
class PaginatedResponseDanfeType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[DanfeType]


@pydantic_type(model=DanfeLastSevenDaysDTO, all_fields=True)
class DanfeLastSevenDaysType:
    pass


@strawberry.type
class PaginatedResponseDanfeLastSevenDaysType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[DanfeLastSevenDaysType]


@pydantic_type(model=DanfeMonthlyDTO, all_fields=True)
class DanfeMonthlyType:
    pass


@strawberry.type
class PaginatedResponseDanfeMonthlyType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[DanfeMonthlyType]
