import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.core import connection
from app.presentation.graphql_router import get_graphql_routers

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):

    # Startup
    logger.info("===========================")
    logger.info("FastAPI iniciado")
    logger.info("SQLAlchemy ORM inicializado")
    logger.info("===========================")

    yield  # Mantém a aplicação rodando

    # Shutdown
    logger.info("Encerrando aplicação e liberando recursos SQLAlchemy")
    await connection.engine.dispose()
    logger.info("Pool de conexões SQLAlchemy encerrado com sucesso")


# Configuração Principal do FastAPI
app = FastAPI(
    title="FastAPI",
    description="API GraphQL",
    version="1.0",
    lifespan=lifespan,
)


# Registrando todos os routers GraphQL dinamicamente
for prefix, router in get_graphql_routers():
    app.include_router(router=router, prefix=prefix)


@app.get("/")
def root():
    return {"message": "Projeto GraphQL em execução"}
