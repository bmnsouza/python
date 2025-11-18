from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schemas.contribuinte_schema import PaginatedResponse, Contribuinte, ContribuinteCreate, ContribuinteUpdate
from app.database import get_session
from app.fastapi.crud.contribuinte_crud import get_contribuintes_danfe_endereco, get_contribuintes_paginado, get_contribuintes, get_contribuinte, create_contribuinte, update_contribuinte, delete_contribuinte


router = APIRouter(prefix="/contribuinte", tags=["Contribuinte"])

@router.get("/danfe-endereco")
async def listar_contribuintes_danfe_endereco(filtro_nome: str, page: int = 1, db: AsyncSession = Depends(get_session)):
    result = await get_contribuintes_danfe_endereco(db, filtro_nome, page)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/paginado", response_model=PaginatedResponse)
async def listar_contribuintes_paginado(page: int = 1, db: AsyncSession = Depends(get_session)):
    result = await get_contribuintes_paginado(db, page)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/", response_model=List[Contribuinte])
async def listar_contribuintes(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    return await get_contribuintes(db, skip=skip, limit=limit)


@router.get("/{cd_contribuinte}", response_model=Contribuinte)
async def obter_contribuinte(cd_contribuinte: str, db: AsyncSession = Depends(get_session)):
    db_contribuinte = await get_contribuinte(db, cd_contribuinte)
    if not db_contribuinte:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return db_contribuinte


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
