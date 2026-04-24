import strawberry
from strawberry.fastapi import GraphQLRouter

from app.database.core.context import get_context
from app.presentation.resolvers.contribuinte_resolver import ContribuinteQuery
from app.presentation.resolvers.danfe_resolver import DanfeQuery
from app.presentation.resolvers.endereco_resolver import EnderecoQuery


@strawberry.type
class Query(ContribuinteQuery, DanfeQuery, EnderecoQuery):
    pass


def get_graphql_routers():
    schema = strawberry.Schema(query=Query)
    router = GraphQLRouter(schema=schema, context_getter=get_context)
    return [("/graphql", router)]
