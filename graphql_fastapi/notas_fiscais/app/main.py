from contextlib import asynccontextmanager

import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.core.logger import app_logger
from app.database import config, connection
from app.database.context import get_context
from app.fastapi.router import api_router
from app.graphql.schema.mutation import Mutation
from app.graphql.schema.query import Query
from app.middleware.logging_middleware import LoggingMiddleware


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # Startup
    app_logger.info("==========================================")
    app_logger.info("GraphQL API Notas Fiscais iniciada.")
    app_logger.info("Oracle User:........ %s", config.ORACLE_USER)
    app_logger.info("Oracle Password....: %s", config.ORACLE_PASSWORD)
    app_logger.info("Oracle DSN.........: %s", config.ORACLE_DSN)
    app_logger.info("Oracle Service Name: %s", config.ORACLE_SERVICE_NAME)
    app_logger.info("==========================================")
    app_logger.info("SQLAlchemy ORM inicializado (pool interno ativo).")

    yield  # Mantém a aplicação rodando

    # Shutdown
    app_logger.info("Encerrando aplicação e liberando recursos SQLAlchemy.")
    await connection.engine.dispose()
    app_logger.info("Pool de conexões SQLAlchemy encerrado com sucesso.")


# Configuração Principal do FastAPI
app = FastAPI(
    title="GraphQL API e FastAPI Notas Fiscais",
    description="API com auditoria SQL, logs e alta performance.",
    version="1.0",
    lifespan=lifespan,
)

# REST
app.include_router(api_router)

# GraphQL
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)
app.include_router(graphql_app, prefix="/graphql")

# Adiciona middleware global
app.add_middleware(LoggingMiddleware)


@app.get("/")
def root():
    return {"message": "GraphQL API e FastAPI Notas Fiscais em execução."}
