import strawberry
from strawberry.fastapi import GraphQLRouter

from app.database.core.context import get_context

from .resolvers.contribuinte_resolver import ContribuinteQuery
from .resolvers.danfe_resolver import DanfeQuery
from .resolvers.endereco_resolver import EnderecoQuery

GRAPHQL_MODULES = [
    ("/graphql/contribuinte", ContribuinteQuery),
    ("/graphql/danfe", DanfeQuery),
    ("/graphql/endereco", EnderecoQuery),
]


def get_graphql_routers():
    routers = []
    for prefix, query_cls in GRAPHQL_MODULES:
        schema = strawberry.Schema(query=query_cls)
        router = GraphQLRouter(schema=schema, context_getter=get_context)
        routers.append((prefix, router))
    return routers
