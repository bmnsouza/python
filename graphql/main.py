import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.core.db import shutdown_db
from app.presentation.graphql_router import get_graphql_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    logger.info("===========================")
    logger.info("FastAPI iniciado")
    logger.info("SQLAlchemy ORM inicializado")
    logger.info("===========================")

    yield

    logger.info("Encerrando aplicação e liberando recursos SQLAlchemy")
    await shutdown_db()
    logger.info("Pool de conexões SQLAlchemy encerrado com sucesso")


app = FastAPI(
    title="FastAPI",
    description="API GraphQL",
    version="1.0",
    lifespan=lifespan,
)

# Registrando o router GraphQL dinamicamente
prefix, router = get_graphql_router()
app.include_router(router=router, prefix=prefix)


@app.get("/")
def root():
    return {"message": "Projeto GraphQL em execução"}
