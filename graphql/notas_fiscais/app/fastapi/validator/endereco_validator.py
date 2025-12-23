from typing import Optional
from pydantic import BaseModel, Field


class EnderecoParams(BaseModel):
    cd_contribuinte: Optional[str] = Field(default=None, min_length=9, max_length=20)
    logradouro: Optional[str] = Field(default=None, min_length=5, max_length=200)
    municipio: Optional[str] = Field(default=None, min_length=5, max_length=100)
    uf: Optional[str] = Field(default=None, min_length=2, max_length=2)


class EnderecoPath(BaseModel):
    id_endereco: int = Field(..., max_digits=10)
