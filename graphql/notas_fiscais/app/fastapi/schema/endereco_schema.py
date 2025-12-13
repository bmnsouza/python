from typing import Optional
from pydantic import BaseModel

from app.fastapi.validators.contribuinte_validator import CD_CONTRIBUINTE_FIELD
from app.fastapi.validators.endereco_validator import LOGRADOURO_FIELD, MUNICIPIO_FIELD, UF_FIELD


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
    logradouro: str = LOGRADOURO_FIELD
    municipio: str = MUNICIPIO_FIELD
    uf: str = UF_FIELD


class EnderecoCreate(EnderecoUpdate):
    cd_contribuinte: str = CD_CONTRIBUINTE_FIELD
