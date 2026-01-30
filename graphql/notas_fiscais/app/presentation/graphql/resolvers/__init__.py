import strawberry

from app.presentation.graphql.resolvers.contribuinte_resolver import ContribuinteQuery
from app.presentation.graphql.resolvers.danfe_resolver import DanfeQuery
from app.presentation.graphql.resolvers.endereco_resolver import EnderecoQuery


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
