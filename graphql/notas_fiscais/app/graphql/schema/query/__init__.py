import strawberry

from app.graphql.schema.query.contribuinte_query import ContribuinteQuery
from app.graphql.schema.query.danfe_query import DanfeQuery
from app.graphql.schema.query.endereco_query import EnderecoQuery


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
