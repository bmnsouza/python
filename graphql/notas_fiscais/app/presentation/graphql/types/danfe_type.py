from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.danfe_dto import DanfeListDTO, DanfeLastSevenDaysDTO, DanfeMonthlyDTO
from app.presentation.graphql.types.pagination_type import PaginationType

@pydantic_type(model=DanfeListDTO, all_fields=True)
class DanfeListType:
    pass


@strawberry.type
class PaginatedResponseDanfeListType:
    pagination: PaginationType
    items: List[DanfeListType]


@pydantic_type(model=DanfeLastSevenDaysDTO, all_fields=True)
class DanfeLastSevenDaysType:
    pass


@strawberry.type
class PaginatedResponseDanfeLastSevenDaysType:
    pagination: PaginationType
    items: List[DanfeLastSevenDaysType]


@pydantic_type(model=DanfeMonthlyDTO, all_fields=True)
class DanfeMonthlyType:
    pass


@strawberry.type
class PaginatedResponseDanfeMonthlyType:
    pagination: PaginationType
    items: List[DanfeMonthlyType]
