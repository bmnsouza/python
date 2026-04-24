from app.presentation.enums.endereco_enum import UF
from app.presentation.filters.base.base_filter import BaseFilter


class EnderecoFilter(BaseFilter):
    cnpj: str


class EnderecosFilter(BaseFilter):
    uf: UF
    municipio: str
