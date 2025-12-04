from typing import Optional

from pydantic import BaseModel


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


class EnderecoCreate(BaseModel):
    cd_contribuinte: str
    logradouro: str
    municipio: str
    uf: str


class EnderecoUpdate(BaseModel):
    logradouro: str
    municipio: str
    uf: str
