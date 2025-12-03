from typing import List, Optional

import strawberry


@strawberry.type
class EnderecoType:
    id_endereco: int
    cd_contribuinte: Optional[str] = None
    logradouro: str
    municipio: str
    uf: str

    @staticmethod
    def from_orm(model) -> "EnderecoType":
        return EnderecoType(
            id_endereco=model.id_endereco,
            cd_contribuinte=model.cd_contribuinte,
            logradouro=model.logradouro,
            municipio=model.municipio,
            uf=model.uf,
        )

@strawberry.type
class SingleResponseEnderecoType:
    data: EnderecoType


@strawberry.type
class PaginatedResponseEnderecoType:
    page: int
    page_size: int
    data: List[EnderecoType]
