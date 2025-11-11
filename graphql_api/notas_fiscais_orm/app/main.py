from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from strawberry.fastapi import GraphQLRouter
import strawberry

from app.schema.query import Query
from app.schema.mutation import Mutation
from app.context import get_context
from app.logger import app_logger
from app import config
from app.middleware.logging_middleware import LoggingMiddleware
from app.database.connection import engine

# ==========================================================
# CONFIGURAÇÃO DO SCHEMA GRAPHQL
# ==========================================================
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema, context_getter=get_context)


# ==========================================================
# CICLO DE VIDA DA APLICAÇÃO (LIFESPAN)
# ==========================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia o ciclo de vida da aplicação (startup/shutdown)."""
    # --- STARTUP ---
    masked_pwd = "*****" if config.ORACLE_PASSWORD else "Not Set"
    app_logger.info("==========================================")
    app_logger.info("GraphQL API Notas Fiscais iniciada.")
    app_logger.info(f"Oracle User: {config.ORACLE_USER}")
    app_logger.info(f"Oracle DSN: {config.ORACLE_DSN}")
    app_logger.info(f"Oracle Password: {masked_pwd}")
    app_logger.info("==========================================")
    app_logger.info("SQLAlchemy ORM inicializado (pool interno ativo).")

    yield  # mantém a aplicação rodando

    # --- SHUTDOWN ---
    app_logger.info("Encerrando aplicação e liberando recursos SQLAlchemy...")
    await engine.dispose()
    app_logger.info("Pool de conexões SQLAlchemy encerrado com sucesso.")


# ==========================================================
# CONFIGURAÇÃO PRINCIPAL DO FASTAPI
# ==========================================================
app = FastAPI(
    title="GraphQL API Notas Fiscais",
    description="API com auditoria SQL, logs e alta performance.",
    version="1.0",
    lifespan=lifespan,
)

# Rota principal GraphQL
app.include_router(graphql_app, prefix="/graphql")

# Adiciona middleware global
app.add_middleware(LoggingMiddleware)


@app.get("/")
def root():
    return {"message": "GraphQL API Notas Fiscais em execução."}
