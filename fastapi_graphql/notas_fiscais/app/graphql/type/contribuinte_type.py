from typing import List, Optional

import strawberry

from app.graphql.type.danfe_type import DanfeType
from app.graphql.type.endereco_type import EnderecoType


@strawberry.type
class ContribuinteType:
    cd_contribuinte: str
    nm_fantasia: str
    cnpj_contribuinte: str
    danfes: Optional[List[DanfeType]] = None
    enderecos: Optional[List[EnderecoType]] = None


@strawberry.type
class ContribuinteSqlType:
    cd_contribuinte: str
    nm_fantasia: str
    cnpj_contribuinte: str


@strawberry.type
class SingleResponseContribuinteType:
    item: Optional[ContribuinteType] = None


@strawberry.type
class PaginatedResponseContribuinteType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[ContribuinteType]


@strawberry.type
class PaginatedResponseContribuinteSqlType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[ContribuinteSqlType]
