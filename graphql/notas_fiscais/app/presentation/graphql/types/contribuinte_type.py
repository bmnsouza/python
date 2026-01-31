from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.contribuinte_dto import ContribuinteDTO


@pydantic_type(model=ContribuinteDTO, all_fields=True)
class ContribuinteType:
    pass


@strawberry.type
class PaginatedResponseContribuinteType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[ContribuinteType]
