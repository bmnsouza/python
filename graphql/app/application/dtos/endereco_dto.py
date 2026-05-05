from pydantic import BaseModel


class EnderecoDTO(BaseModel):
    cnpj_contribuinte: str | None
    logradouro: str | None
    municipio: str | None
    uf: str | None
