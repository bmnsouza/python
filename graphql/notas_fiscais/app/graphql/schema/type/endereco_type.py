from typing import List

import strawberry


@strawberry.type
class EnderecoType:
    id_endereco: int
    cd_contribuinte: str
    logradouro: str
    municipio: str
    uf: str


@strawberry.type
class SingleResponseEnderecoType:
    item: EnderecoType


@strawberry.type
class PaginatedResponseEnderecoType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[EnderecoType]
