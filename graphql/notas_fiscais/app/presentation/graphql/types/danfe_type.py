from datetime import datetime
from decimal import Decimal
from typing import List

import strawberry


@strawberry.type
class DanfeType:
    id_danfe: int
    cd_contribuinte: str
    numero: str
    valor_total: Decimal
    data_emissao: datetime


@strawberry.type
class PaginatedResponseDanfeType:
    offset: int
    limit: int
    total: int
    accept_ranges: int
    items: List[DanfeType]
