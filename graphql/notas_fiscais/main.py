from contextlib import asynccontextmanager

import logging
import strawberry

from strawberry.fastapi import GraphQLRouter

from fastapi import FastAPI

from app.infraestructure.database import connection
from app.infraestructure.database.context import get_context
from app.presentation.graphql.resolvers.contribuinte_resolver import ContribuinteQuery
from app.presentation.graphql.resolvers.danfe_resolver import DanfeQuery
from app.presentation.graphql.resolvers.endereco_resolver import EnderecoQuery

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):

    # Startup
    logger.info("==========================================")
    logger.info("FastAPI iniciado.")
    logger.info("SQLAlchemy ORM inicializado (pool interno ativo).")
    logger.info("==========================================")

    yield  # Mantém a aplicação rodando

    # Shutdown
    logger.info("Encerrando aplicação e liberando recursos SQLAlchemy.")
    await connection.engine.dispose()
    logger.info("Pool de conexões SQLAlchemy encerrado com sucesso.")


# Configuração Principal do FastAPI
app = FastAPI(
    title="FastAPI Notas Fiscais",
    description="API com auditoria SQL, logs e alta performance.",
    version="1.0",
    lifespan=lifespan,
)

# GraphQL
# Contribuinte
schema_contribuinte = strawberry.Schema(query=ContribuinteQuery)
graphql_contribuinte = GraphQLRouter(schema=schema_contribuinte, context_getter=get_context)
app.include_router(router=graphql_contribuinte, prefix="/graphql/contribuinte")

# Danfe
schema_danfe = strawberry.Schema(query=DanfeQuery)
graphql_danfe = GraphQLRouter(schema=schema_danfe, context_getter=get_context)
app.include_router(router=graphql_danfe, prefix="/graphql/danfe")

# Endereco
schema_endereco = strawberry.Schema(query=EnderecoQuery)
graphql_endereco = GraphQLRouter(schema=schema_endereco, context_getter=get_context)
app.include_router(router=graphql_endereco, prefix="/graphql/endereco")


@app.get("/")
def root():
    return {"message": "Projeto Notas Fiscais em execução."}
