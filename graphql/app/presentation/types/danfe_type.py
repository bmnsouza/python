from strawberry.experimental.pydantic import type as strawberry_pydantic_type

from ..dtos.danfe_dto import DanfeDTO


@strawberry_pydantic_type(model=DanfeDTO, all_fields=True)
class DanfeType:
    pass
