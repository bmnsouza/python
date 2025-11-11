import strawberry
from .contribuinte_mutation import ContribuinteMutation
from .danfe_mutation import DanfeMutation
from .endereco_mutation import EnderecoMutation


@strawberry.type
class Mutation(ContribuinteMutation, DanfeMutation, EnderecoMutation):
    """Classe principal que une todas as subqueries"""
    pass