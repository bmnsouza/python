from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.endereco_dto import EnderecoListDTO
from app.presentation.graphql.types.pagination_type import PaginationType


@pydantic_type(model=EnderecoListDTO, all_fields=True)
class EnderecoListType:
    pass


@strawberry.type
class PaginatedResponseEnderecoListType:
    pagination: PaginationType
    items: List[EnderecoListType]
