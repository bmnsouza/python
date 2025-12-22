from typing import Optional
from pydantic import BaseModel, Field


class EnderecoBase(BaseModel):
    cd_contribuinte: Optional[str] = None
    logradouro: Optional[str] = None
    municipio: Optional[str] = None
    uf: Optional[str] = None
    class Config:
        from_attributes = True


class Endereco(EnderecoBase):
    id_endereco: Optional[int] = None
    class Config:
        from_attributes = True


class EnderecoUpdate(BaseModel):
    logradouro: Optional[str] = Field(default=None, min_length=5, max_length=200)
    municipio: Optional[str] = Field(default=None, min_length=5, max_length=100)
    uf: Optional[str] = Field(default=None, min_length=2, max_length=2)


class EnderecoCreate(BaseModel):
    cd_contribuinte: str = Field(..., min_length=9, max_length=20)
    logradouro: str = Field(..., min_length=5, max_length=200)
    municipio: str = Field(..., min_length=5, max_length=100)
    uf: str = Field(..., min_length=2, max_length=2)
