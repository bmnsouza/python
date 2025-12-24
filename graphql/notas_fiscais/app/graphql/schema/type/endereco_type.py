from typing import List, Optional

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
    item: Optional[EnderecoType] = None


@strawberry.type
class PaginatedResponseEnderecoType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[EnderecoType]
