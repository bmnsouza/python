import strawberry

from app.graphql.query.contribuinte_query import ContribuinteQuery
from app.graphql.query.danfe_query import DanfeQuery
from app.graphql.query.endereco_query import EnderecoQuery


@strawberry.type
class Query:
    @strawberry.field
    def contribuinte(self) -> ContribuinteQuery:
        return ContribuinteQuery()

    @strawberry.field
    def danfe(self) -> DanfeQuery:
        return DanfeQuery()

    @strawberry.field
    def endereco(self) -> EnderecoQuery:
        return EnderecoQuery()
