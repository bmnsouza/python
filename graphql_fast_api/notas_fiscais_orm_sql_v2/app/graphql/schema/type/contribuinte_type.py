from typing import List, Optional
import strawberry
from .danfe_type import DanfeType
from .endereco_type import EnderecoType

@strawberry.type
class ContribuinteType:
    cd_contribuinte: str
    nm_fantasia: Optional[str]
    cnpj_contribuinte: str
    danfes: Optional[List[DanfeType]] = None
    enderecos: Optional[List[EnderecoType]] = None

    @staticmethod
    def from_orm(model) -> "ContribuinteType":
        return ContribuinteType(
            cd_contribuinte=model.cd_contribuinte,
            nm_fantasia=model.nm_fantasia,
            cnpj_contribuinte=model.cnpj_contribuinte,
            danfes=[DanfeType.from_orm(d) for d in model.danfes] if model.danfes else [],
            enderecos=[EnderecoType.from_orm(e) for e in model.enderecos] if model.enderecos else [],
        )


@strawberry.type
class ContribuinteDenfeEnderecoType:
    cd_contribuinte: str
    cnpj_contribuinte: Optional[str]
    nm_fantasia: Optional[str]
    numero: Optional[str]
    data_emissao: Optional[str]
    valor_total: Optional[float]
    logradouro: Optional[str]
    municipio: Optional[str]
    uf: Optional[str]


@strawberry.type
class PaginatedType:
    page: int
    page_size: int
    data: List[ContribuinteType]
