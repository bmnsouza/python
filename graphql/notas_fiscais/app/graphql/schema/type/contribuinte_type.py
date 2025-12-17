from typing import List, Optional

import strawberry

from app.graphql.schema.type.danfe_type import DanfeType
from app.graphql.schema.type.endereco_type import EnderecoType


@strawberry.type
class ContribuinteType:
    cd_contribuinte: str
    nm_fantasia: str
    cnpj_contribuinte: str
    danfes: Optional[List[DanfeType]] = None
    enderecos: Optional[List[EnderecoType]] = None


@strawberry.type
class SingleResponseContribuinteType:
    item: ContribuinteType


@strawberry.type
class PaginatedResponseContribuinteType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[ContribuinteType]
