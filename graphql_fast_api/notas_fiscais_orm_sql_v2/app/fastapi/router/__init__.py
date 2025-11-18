from fastapi import APIRouter

# Importa todos os routers individuais
from . import contribuinte_router, danfe_router, endereco_router

# Cria um router "raiz" que engloba todos
api_router = APIRouter()

# Inclui cada router específico
api_router.include_router(contribuinte_router.router)
api_router.include_router(danfe_router.router)
api_router.include_router(endereco_router.router)
