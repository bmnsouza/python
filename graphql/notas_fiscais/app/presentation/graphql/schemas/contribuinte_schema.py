from typing import Optional
from pydantic import BaseModel, Field

from app.presentation.graphql.inputs.order_input import OrderDirection


class ContribuinteInputSchema(BaseModel):
    cd_contribuinte: Optional[str] = Field(default=None, min_length=9, max_length=20)
    cnpj_contribuinte: Optional[str] = Field(default=None, min_length=14, max_length=14)
    nm_fantasia: Optional[str] = Field(default=None, min_length=5, max_length=200)


class ContribuinteOrderSchema(BaseModel):
    cd_contribuinte: Optional[OrderDirection] = Field(default=None)
    cnpj_contribuinte: Optional[OrderDirection] = Field(default=None)
    nm_fantasia: Optional[OrderDirection] = Field(default=None)
