from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from strawberry.fastapi import GraphQLRouter
import strawberry
import time
import uuid

from app.schema.query import Query
from app.schema.mutation import Mutation

from app.database import init_pool
from app.logger import app_logger
from app import config


# ==========================================================
# CONFIGURAÇÃO DO SCHEMA GRAPHQL
# ==========================================================
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)


# ==========================================================
# CONTEXTO DE VIDA (LIFESPAN)
# ==========================================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia o ciclo de vida da aplicação (startup/shutdown)."""
    # --- STARTUP ---
    init_pool()

    masked_pwd = "*****" if config.ORACLE_PASSWORD else None
    app_logger.info("==========================================")
    app_logger.info("GraphQL API Notas Fiscais iniciada.")
    app_logger.info(f"Oracle User: {config.ORACLE_USER}")
    app_logger.info(f"Oracle DSN: {config.ORACLE_DSN}")
    app_logger.info(f"Oracle Password: {masked_pwd}")
    app_logger.info("==========================================")
    app_logger.info("Pool Oracle inicializado e API pronta para uso.")

    yield  # <- mantém a API ativa enquanto roda

    # --- SHUTDOWN ---
    app_logger.info("Encerrando aplicação e liberando recursos Oracle...")


# ==========================================================
# CONFIGURAÇÃO PRINCIPAL DO FASTAPI
# ==========================================================
app = FastAPI(
    title="GraphQL API Notas Fiscais",
    description="API com auditoria SQL, logs e alta performance.",
    version="1.1",
    lifespan=lifespan,  # substitui o on_event("startup")
)

app.include_router(graphql_app, prefix="/graphql")


# ==========================================================
# MIDDLEWARE DE AUDITORIA / LOG DE REQUISIÇÕES
# ==========================================================
@app.middleware("http")
async def log_request_timing(request: Request, call_next):
    """Auditoria e métricas de tempo por requisição HTTP."""
    request_id = str(uuid.uuid4())[:8]
    start = time.perf_counter()
    app_logger.info(f"[{request_id}] Início da requisição: {request.method} {request.url.path}")

    response = await call_next(request)

    duration_ms = (time.perf_counter() - start) * 1000
    app_logger.info(f"[{request_id}] Finalizada em {duration_ms:.2f} ms - Status {response.status_code}")

    return response


# ==========================================================
# ENDPOINT PRINCIPAL (teste rápido)
# ==========================================================
@app.get("/")
def root():
    return {
        "message": "GraphQL API Notas Fiscais em execução com auditoria SQL e logs de performance."
    }
