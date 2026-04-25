import strawberry
from strawberry.fastapi import GraphQLRouter

from app.database.core.db import get_graphql_context
from app.presentation.resolvers.contribuinte_resolver import ContribuinteQuery
from app.presentation.resolvers.danfe_resolver import DanfeQuery
from app.presentation.resolvers.endereco_resolver import EnderecoQuery


@strawberry.type
class Query(ContribuinteQuery, DanfeQuery, EnderecoQuery):
    pass


def _build_schema() -> strawberry.Schema:
    return strawberry.Schema(query=Query)


def get_graphql_router() -> tuple[str, GraphQLRouter]:
    router = GraphQLRouter(
        schema=_build_schema(),
        context_getter=get_graphql_context,
    )
    return "/graphql", router
