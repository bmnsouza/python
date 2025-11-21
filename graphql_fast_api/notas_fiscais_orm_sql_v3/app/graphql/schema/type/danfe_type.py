from typing import Optional, List
from datetime import datetime
import strawberry


@strawberry.type
class DanfeType:
    id_danfe: int
    cd_contribuinte: Optional[str] = None
    numero: str
    valor_total: float
    data_emissao: Optional[datetime]

    @staticmethod
    def from_orm(model) -> "DanfeType":
        return DanfeType(
            id_danfe=model.id_danfe,
            cd_contribuinte=model.cd_contribuinte,
            numero=model.numero,
            valor_total=model.valor_total,
            data_emissao=model.data_emissao,
        )


@strawberry.type
class SingleResponseType:
    data: DanfeType


@strawberry.type
class PaginatedResponseType:
    page: int
    page_size: int
    data: List[DanfeType]
