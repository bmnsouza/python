from typing import Optional

import strawberry

from app.presentation.graphql.inputs.order_input import OrderDirection


@strawberry.input
class EnderecoFilterInput:
    cd_contribuinte: Optional[str] = None
    logradouro: Optional[str] = None
    municipio: Optional[str] = None
    uf: Optional[str] = None


@strawberry.input
class EnderecoOrderInput:
    cd_contribuinte: Optional[OrderDirection] = None
    logradouro: Optional[OrderDirection] = None
    municipio: Optional[OrderDirection] = None
    uf: Optional[OrderDirection] = None
