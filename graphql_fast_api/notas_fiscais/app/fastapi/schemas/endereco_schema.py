from typing import Optional
from pydantic import BaseModel

class EnderecoBase(BaseModel):
    cd_contribuinte: str
    logradouro: Optional[str] = None
    municipio: Optional[str] = None
    uf: Optional[str] = None

class EnderecoCreate(EnderecoBase):
    pass

class EnderecoUpdate(BaseModel):
    logradouro: Optional[str] = None
    municipio: Optional[str] = None
    uf: Optional[str] = None

class Endereco(EnderecoBase):
    id_endereco: int

    class Config:
        from_attributes = True
