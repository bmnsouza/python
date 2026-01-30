from typing import List

import strawberry


@strawberry.type
class ContribuinteType:
    cd_contribuinte: str
    nm_fantasia: str
    cnpj_contribuinte: str


@strawberry.type
class PaginatedResponseContribuinteType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[ContribuinteType]
