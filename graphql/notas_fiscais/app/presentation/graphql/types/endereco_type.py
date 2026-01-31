from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.endereco_dto import EnderecoDTO
from app.presentation.graphql.types.pagination_type import PaginationType


@pydantic_type(model=EnderecoDTO, all_fields=True)
class EnderecoType:
    pass


@strawberry.type
class PaginatedResponseEnderecoType:
    pagination: PaginationType
    items: List[EnderecoType]
