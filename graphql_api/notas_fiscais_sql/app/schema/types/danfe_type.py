import strawberry
from typing import List, Optional
from datetime import datetime


@strawberry.type
class DanfeType:
    id_danfe: Optional[int]
    numero: Optional[str]
    valor_total: Optional[float]
    data_emissao: Optional[datetime]
    cd_contribuinte: Optional[str] = None

@strawberry.input
class FiltroDanfeInput:
    numero: Optional[str] = None
    valor_minimo: Optional[float] = None
    valor_maximo: Optional[float] = None
    data_inicial: Optional[datetime] = None
    data_final: Optional[datetime] = None
    cd_contribuinte: Optional[str] = None

@strawberry.type
class PaginacaoDanfe:
    total_registros: int
    proximo_cursor: Optional[int]
    danfes: List[DanfeType]

def map_row_to_danfe(row: dict) -> DanfeType:
    """Converte dicionário do Oracle para objeto Danfe."""
    return DanfeType(
        id_danfe=row.get("id_danfe"),
        numero=row.get("numero"),
        valor_total=row.get("valor_total"),
        data_emissao=row.get("data_emissao"),
        cd_contribuinte=row.get("cd_contribuinte")
    )
