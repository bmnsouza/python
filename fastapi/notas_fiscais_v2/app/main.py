from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from fastapi.exceptions import RequestValidationError

from app.utils.handler_utils import http_exception_handler, validation_exception_handler

from app.core.logger import app_logger
from app.database import config, connection
from app.fastapi.router import api_router
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

# Adiciona middleware global
app.add_middleware(LoggingMiddleware)

# Adiciona handler global
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get("/")
def root():
    return {"message": "FastAPI Notas Fiscais em execução."}
