from typing import Optional

import strawberry

from app.presentation.graphql.inputs.order_input import OrderDirection


@strawberry.input
class ContribuinteFilterInput:
    cd_contribuinte: Optional[str] = None
    cnpj_contribuinte: Optional[str] = None
    nm_fantasia: Optional[str] = None


@strawberry.input
class ContribuinteOrderInput:
    cd_contribuinte: Optional[OrderDirection] = None
    cnpj_contribuinte: Optional[OrderDirection] = None
    nm_fantasia: Optional[OrderDirection] = None
