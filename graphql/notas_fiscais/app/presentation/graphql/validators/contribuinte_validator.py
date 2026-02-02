from pydantic import BaseModel, Field

from app.domain.values.contribuinte_value import CdContribuinte, CnpjContribuinte
from app.presentation.graphql.inputs.order_input import OrderDirection


class ContribuinteListFilterInputValidator(BaseModel):
    cd_contribuinte: CdContribuinte | None = None
    cnpj_contribuinte: CnpjContribuinte | None = None
    nm_fantasia: str | None = Field(default=None, min_length=5, max_length=200)


class ContribuinteListOrderInputValidator(BaseModel):
    cd_contribuinte: OrderDirection | None = Field(default=None)
    cnpj_contribuinte: OrderDirection | None = Field(default=None)
    nm_fantasia: OrderDirection | None = Field(default=None)
