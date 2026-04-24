from strawberry.experimental.pydantic import input as strawberry_pydantic_input

from app.presentation.filters.danfe_filter import DanfeFilter, DanfesFilter


@strawberry_pydantic_input(model=DanfeFilter, all_fields=True)
class DanfeInput:
    pass


@strawberry_pydantic_input(model=DanfesFilter, all_fields=True)
class DanfesInput:
    pass
