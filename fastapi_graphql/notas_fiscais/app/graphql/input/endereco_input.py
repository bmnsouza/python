from typing import Optional

import strawberry


@strawberry.input
class EnderecoParamsInput:
    cd_contribuinte: Optional[str] = None
    logradouro: Optional[str] = None
    municipio: Optional[str] = None
    uf: Optional[str] = None


@strawberry.input
class EnderecoParamInput:
    id_endereco: int
