from pydantic import BaseModel, Field

from app.presentation.graphql.inputs.order_input import OrderDirection


class ContribuinteInputSchema(BaseModel):
    cd_contribuinte: str | None = Field(default=None, min_length=9, max_length=20)
    cnpj_contribuinte: str | None = Field(default=None, min_length=14, max_length=14)
    nm_fantasia: str | None = Field(default=None, min_length=5, max_length=200)


class ContribuinteOrderSchema(BaseModel):
    cd_contribuinte: OrderDirection | None = Field(default=None)
    cnpj_contribuinte: OrderDirection | None = Field(default=None)
    nm_fantasia: OrderDirection | None = Field(default=None)
