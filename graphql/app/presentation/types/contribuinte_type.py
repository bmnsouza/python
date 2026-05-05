from strawberry.experimental.pydantic import type as strawberry_pydantic_type

from app.application.dtos.contribuinte_dto import ContribuinteDTO


@strawberry_pydantic_type(model=ContribuinteDTO, all_fields=True)
class ContribuinteType:
    pass
