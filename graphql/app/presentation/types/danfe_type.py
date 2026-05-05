from strawberry.experimental.pydantic import type as strawberry_pydantic_type

from app.presentation.dtos.danfe_dto import DanfeDTO, DanfeItemDTO


@strawberry_pydantic_type(model=DanfeItemDTO, all_fields=True)
class DanfeItemType:
    pass


@strawberry_pydantic_type(model=DanfeDTO, all_fields=True)
class DanfeType:
    pass
