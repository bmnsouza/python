import strawberry
from typing import List, Optional
from .danfe_type import DanfeType
from .endereco_type import EnderecoType


@strawberry.type
class ContribuinteType:
    cd_contribuinte: str
    nm_fantasia: Optional[str]
    cnpj_contribuinte: str
    enderecos: Optional[List[EnderecoType]] = None
    danfes: Optional[List[DanfeType]] = None

def map_row_to_contribuinte(row: dict) -> ContribuinteType:
    """Converte dicionário do Oracle para objeto Contribuinte."""
    return ContribuinteType(
        cd_contribuinte=row.get("cd_contribuinte"),
        nm_fantasia=row.get("nm_fantasia"),
        cnpj_contribuinte=row.get("cnpj_contribuinte")
    )
