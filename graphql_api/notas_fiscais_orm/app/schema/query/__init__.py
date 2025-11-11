import strawberry
from .contribuinte_query import ContribuinteQuery
from .danfe_query import DanfeQuery
from .endereco_query import EnderecoQuery

@strawberry.type
class Query(ContribuinteQuery, DanfeQuery, EnderecoQuery):
    """Combina todas as queries em um único schema GraphQL."""
    pass
