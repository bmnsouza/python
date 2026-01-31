from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.contribuinte_dto import ContribuinteDTO
from app.presentation.graphql.types.pagination_type import PaginationType


@pydantic_type(model=ContribuinteDTO, all_fields=True)
class ContribuinteType:
    pass


@strawberry.type
class PaginatedResponseContribuinteType:
    pagination: PaginationType
    items: List[ContribuinteType]
