from contextlib import asynccontextmanager

import strawberry
from strawberry.fastapi import GraphQLRouter

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.core.logger import app_logger
from app.database import config, connection
from app.database.context import get_context
from app.fastapi.router import api_router
from app.fastapi.utils.handler_util import http_exception_handler, validation_exception_handler
from app.graphql.schema.query.contribuinte_query import ContribuinteQuery
from app.graphql.schema.query.danfe_query import DanfeQuery
from app.graphql.schema.query.endereco_query import EnderecoQuery
from app.middleware.logging_middleware import LoggingMiddleware


@asynccontextmanager
async def lifespan(_app: FastAPI):

    # Startup
    app_logger.info("==========================================")
    app_logger.info("FastAPI Notas Fiscais iniciada.")
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
    title="FastAPI Notas Fiscais",
    description="API com auditoria SQL, logs e alta performance.",
    version="1.0",
    lifespan=lifespan,
)

# REST
app.include_router(api_router)


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


# Adiciona middleware global
app.add_middleware(LoggingMiddleware)


# Adiciona handler global
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get("/")
def root():
    return {"message": "Projeto Notas Fiscais em execução."}
