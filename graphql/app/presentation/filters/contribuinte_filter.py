from .base.base_filter import BaseFilter


class ContribuinteFilter(BaseFilter):
    cnpj: str


class ContribuintesFilter(BaseFilter):
    nmFantasia: str
