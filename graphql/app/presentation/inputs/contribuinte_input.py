from strawberry.experimental.pydantic import input as strawberry_pydantic_input

from ..filters.contribuinte_filter import ContribuinteFilter, ContribuintesFilter


@strawberry_pydantic_input(model=ContribuinteFilter, all_fields=True)
class ContribuinteInput:
    pass


@strawberry_pydantic_input(model=ContribuintesFilter, all_fields=True)
class ContribuintesInput:
    pass
