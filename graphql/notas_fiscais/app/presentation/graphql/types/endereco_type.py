from typing import List

import strawberry
from strawberry.experimental.pydantic import type as pydantic_type

from app.application.dto.endereco_dto import EnderecoDTO


@pydantic_type(model=EnderecoDTO, all_fields=True)
class EnderecoType:
    pass


@strawberry.type
class PaginatedResponseEnderecoType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[EnderecoType]
