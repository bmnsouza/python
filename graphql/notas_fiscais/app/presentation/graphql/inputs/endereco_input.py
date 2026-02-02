import strawberry

from app.presentation.graphql.inputs.order_input import OrderDirection


@strawberry.input
class EnderecoFilterInput:
    cd_contribuinte: str | None = None
    logradouro: str | None = None
    municipio: str | None = None
    uf: str | None = None


@strawberry.input
class EnderecoOrderInput:
    cd_contribuinte: OrderDirection | None = None
    logradouro: OrderDirection | None = None
    municipio: OrderDirection | None = None
    uf: OrderDirection | None = None
