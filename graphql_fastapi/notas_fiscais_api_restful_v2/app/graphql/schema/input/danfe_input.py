from datetime import datetime
from typing import Optional

import strawberry


@strawberry.input
class DanfeFiltroInput:
    cd_contribuinte: Optional[str] = None
    numero: Optional[str] = None
    valor_minimo: Optional[float] = None
    valor_maximo: Optional[float] = None
    data_inicial: Optional[datetime] = None
    data_final: Optional[datetime] = None
