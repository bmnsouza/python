from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.contribuinte_danfe_dto import ContribuinteDanfeMonthlyDTO
from app.presentation.graphql.types.pagination_type import PaginationType


@pydantic_type(model=ContribuinteDanfeMonthlyDTO, all_fields=True)
class ContribuinteDanfeMonthlyType:
    pass


@strawberry.type
class PaginatedResponseContribuinteDanfeMonthlyType:
    pagination: PaginationType
    items: List[ContribuinteDanfeMonthlyType]
