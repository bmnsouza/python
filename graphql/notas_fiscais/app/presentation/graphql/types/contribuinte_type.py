from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.contribuinte_dto import ContribuinteListDTO
from app.presentation.graphql.types.pagination_type import PaginationType


@pydantic_type(model=ContribuinteListDTO, all_fields=True)
class ContribuinteListType:
    pass


@strawberry.type
class PaginatedResponseContribuinteListType:
    pagination: PaginationType
    items: List[ContribuinteListType]
