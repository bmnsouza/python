from contextlib import asynccontextmanager

import logging

from fastapi import FastAPI

from app.infraestructure.database import connection
from app.presentation.graphql.graphql_router import get_graphql_routers

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


# Registrando todos os routers GraphQL dinamicamente
for prefix, router in get_graphql_routers():
    app.include_router(router=router, prefix=prefix)


@app.get("/")
def root():
    return {"message": "Projeto Notas Fiscais em execução."}
