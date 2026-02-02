from typing import Optional

from pydantic import BaseModel, Field

from app.presentation.graphql.inputs.order_input import OrderDirection


class EnderecoInputSchema(BaseModel):
    cd_contribuinte: Optional[str] = Field(default=None, min_length=9, max_length=20)
    logradouro: Optional[str] = Field(default=None, min_length=5, max_length=200)
    municipio: Optional[str] = Field(default=None, min_length=5, max_length=100)
    uf: Optional[str] = Field(default=None, min_length=2, max_length=2)


class EnderecoOrderSchema(BaseModel):
    cd_contribuinte: Optional[OrderDirection] = Field(default=None)
    logradouro: Optional[OrderDirection] = Field(default=None)
    municipio: Optional[OrderDirection] = Field(default=None)
    uf: Optional[OrderDirection] = Field(default=None)
