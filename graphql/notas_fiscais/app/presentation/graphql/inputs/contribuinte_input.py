import strawberry

from app.presentation.graphql.inputs.order_input import OrderDirection


@strawberry.input
class ContribuinteFilterInput:
    cd_contribuinte: str | None = None
    cnpj_contribuinte: str | None = None
    nm_fantasia: str | None = None


@strawberry.input
class ContribuinteOrderInput:
    cd_contribuinte: OrderDirection | None = None
    cnpj_contribuinte: OrderDirection | None = None
    nm_fantasia: OrderDirection | None = None
