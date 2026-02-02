from strawberry.fastapi import GraphQLRouter
import strawberry

from app.infraestructure.database.context import get_context
from app.presentation.graphql.resolvers.contribuinte_danfe_resolver import ContribuinteDanfeQuery
from app.presentation.graphql.resolvers.contribuinte_resolver import ContribuinteQuery
from app.presentation.graphql.resolvers.danfe_resolver import DanfeQuery
from app.presentation.graphql.resolvers.endereco_resolver import EnderecoQuery


# Lista de módulos GraphQL: (prefixo, query)
GRAPHQL_MODULES = [
    ("/graphql/contribuinte-danfe", ContribuinteDanfeQuery),
    ("/graphql/contribuinte", ContribuinteQuery),
    ("/graphql/danfe", DanfeQuery),
    ("/graphql/endereco", EnderecoQuery)
]


def get_graphql_routers():
    routers = []
    for prefix, query_cls in GRAPHQL_MODULES:
        schema = strawberry.Schema(query=query_cls)
        router = GraphQLRouter(schema=schema, context_getter=get_context)
        routers.append((prefix, router))
    return routers
