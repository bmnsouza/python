from strawberry.experimental.pydantic import type as strawberry_pydantic_type

from app.presentation.dtos.endereco_dto import EnderecoDTO


@strawberry_pydantic_type(model=EnderecoDTO, all_fields=True)
class EnderecoType:
    pass
