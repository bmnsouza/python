from strawberry.experimental.pydantic import input as strawberry_pydantic_input

from ..filters.endereco_filter import EnderecoFilter, EnderecosFilter


@strawberry_pydantic_input(model=EnderecoFilter, all_fields=True)
class EnderecoInput:
    pass


@strawberry_pydantic_input(model=EnderecosFilter, all_fields=True)
class EnderecosInput:
    pass
