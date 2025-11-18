from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schema.contribuinte_schema import Contribuinte, ContribuinteCreate, ContribuinteUpdate, Response, PaginatedResponse
from app.database.session import get_session
from app.core.pagination import DEFAULT_PAGE
from app.repository.contribuinte_repository import get_contribuintes_danfe_endereco, create_contribuinte, update_contribuinte, delete_contribuinte
from app.service import contribuinte_service


router = APIRouter(prefix="/contribuinte", tags=["Contribuinte"])

@router.get("/danfe-endereco")
async def listar_contribuintes_danfe_endereco(filtro_nome: str, page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    result = await get_contribuintes_danfe_endereco(db, filtro_nome, page)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/", response_model=PaginatedResponse)
async def get_contribuintes(page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    result = await contribuinte_service.get_contribuintes(page, db)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/cd", response_model=Response)
async def get_contribuinte_por_cd(cd_contribuinte: str, db: AsyncSession = Depends(get_session)):
    result = await contribuinte_service.get_contribuinte_por_cd(cd_contribuinte, db)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/cnpj", response_model=Response)
async def get_contribuinte_por_cnpj(cnpj_contribuinte: str, db: AsyncSession = Depends(get_session)):
    result = await contribuinte_service.get_contribuinte_por_cnpj(cnpj_contribuinte, db)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.post("/", response_model=Contribuinte, status_code=201)
async def criar_contribuinte(contribuinte: ContribuinteCreate, db: AsyncSession = Depends(get_session)):
    return await create_contribuinte(db, contribuinte)


@router.put("/{cd_contribuinte}", response_model=Contribuinte)
async def atualizar_contribuinte(cd_contribuinte: str, updates: ContribuinteUpdate, db: AsyncSession = Depends(get_session)):
    db_contribuinte = await update_contribuinte(db, cd_contribuinte, updates)
    if not db_contribuinte:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return db_contribuinte


@router.delete("/{cd_contribuinte}", status_code=204)
async def excluir_contribuinte(cd_contribuinte: str, db: AsyncSession = Depends(get_session)):
    db_contribuinte = await delete_contribuinte(db, cd_contribuinte)
    if not db_contribuinte:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return {"ok": True, "message": "Contribuinte excluído com sucesso"}
