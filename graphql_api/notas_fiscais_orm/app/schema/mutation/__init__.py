import strawberry
from .contribuinte_mutation import ContribuinteMutation
from .endereco_mutation import EnderecoMutation
from .danfe_mutation import DanfeMutation


@strawberry.type
class Mutation(ContribuinteMutation, EnderecoMutation, DanfeMutation):
    """Combina todas as mutations em um único schema GraphQL."""
    pass
