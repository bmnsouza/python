import strawberry

from app.graphql.schema.query.contribuinte_query import ContribuinteQuery
# from app.graphql.schema.query.danfe_query import DanfeQuery
# from app.graphql.schema.query.endereco_query import EnderecoQuery


@strawberry.type
class Query(ContribuinteQuery):
    pass


# @strawberry.type
# class Query(ContribuinteQuery, DanfeQuery, EnderecoQuery):
#     pass
