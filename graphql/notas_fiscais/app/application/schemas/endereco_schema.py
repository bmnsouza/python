from pydantic import BaseModel


class Endereco(BaseModel):
    id_endereco: int
    cd_contribuinte: str
    logradouro: str
    municipio: str
    uf: str
