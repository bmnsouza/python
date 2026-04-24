from app.presentation.filters.base.base_filter import BaseFilter


class DanfeFilter(BaseFilter):
    numero: str


class DanfesFilter(BaseFilter):
    cnpj: str
    ano: int
