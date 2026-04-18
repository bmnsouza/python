from .base.base_filter import BaseFilter


class EnderecoFilter(BaseFilter):
    cnpj: str


class EnderecosFilter(BaseFilter):
    uf: str
    municipio: str
