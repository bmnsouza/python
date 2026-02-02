from pydantic import BaseModel, Field

from app.domain.values.contribuinte_value import CdContribuinte
from app.presentation.graphql.inputs.order_input import OrderDirection


class EnderecoListFilterInputValidator(BaseModel):
    cd_contribuinte: CdContribuinte | None = None
    logradouro: str | None = Field(default=None, min_length=5, max_length=200)
    municipio: str | None = Field(default=None, min_length=5, max_length=100)
    uf: str | None = Field(default=None, min_length=2, max_length=2)


class EnderecoListOrderInputValidator(BaseModel):
    cd_contribuinte: OrderDirection | None = Field(default=None)
    logradouro: OrderDirection | None = Field(default=None)
    municipio: OrderDirection | None = Field(default=None)
    uf: OrderDirection | None = Field(default=None)
