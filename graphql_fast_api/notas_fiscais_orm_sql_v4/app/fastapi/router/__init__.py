from fastapi import APIRouter

from app.fastapi.router import contribuinte_router, danfe_router, endereco_router


api_router = APIRouter()

# Inclui cada router específico
api_router.include_router(contribuinte_router.router)
api_router.include_router(danfe_router.router)
api_router.include_router(endereco_router.router)
