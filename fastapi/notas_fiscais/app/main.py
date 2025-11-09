from fastapi import FastAPI
from contextlib import asynccontextmanager
from app import database
from app.routers import contribuinte_router, danfe_router, endereco_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Gerencia o ciclo de vida da aplicação (subida e descida)."""
    print("Iniciando API e criando pool de conexões Oracle...")
    database.init_pool()
    print("Pool de conexões Oracle inicializado com sucesso.")

    yield  # API rodando

    if database.pool:
        print("Encerrando pool de conexões Oracle...")
        database.pool.close(force=True)
        print("Pool de conexões Oracle encerrado.")


app = FastAPI(
    title="API de Notas Fiscais",
    version="1.0.0",
    description="API construída com FastAPI e Oracle com pool de conexões.",
    lifespan=lifespan,
)

# Adiciona o router
app.include_router(contribuinte_router.router)
app.include_router(danfe_router.router)
app.include_router(endereco_router.router)

@app.get("/")
def root():
    return {"message": "API de Notas Fiscais em execução"}
