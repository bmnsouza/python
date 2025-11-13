from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schemas.danfe_schema import Danfe, DanfeCreate, DanfeUpdate
from app.database import get_session
from app.fastapi.crud.danfe_crud import get_danfes, get_danfe, create_danfe, update_danfe, delete_danfe


router = APIRouter(prefix="/danfe", tags=["Danfe"])

@router.get("/", response_model=List[Danfe])
async def listar_danfes(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    return await get_danfes(db, skip=skip, limit=limit)

@router.get("/{id_danfe}", response_model=Danfe)
async def obter_danfe(id_danfe: int, db: AsyncSession = Depends(get_session)):
    db_danfe = await get_danfe(db, id_danfe)
    if not db_danfe:
        raise HTTPException(status_code=404, detail="Danfe não encontrado")
    return db_danfe

@router.post("/", response_model=Danfe, status_code=201)
async def criar_danfe(danfe: DanfeCreate, db: AsyncSession = Depends(get_session)):
    return await create_danfe(db, danfe)

@router.put("/{id_danfe}", response_model=Danfe)
async def atualizar_danfe(id_danfe: int, updates: DanfeUpdate, db: AsyncSession = Depends(get_session)):
    db_danfe = await update_danfe(db, id_danfe, updates)
    if not db_danfe:
        raise HTTPException(status_code=404, detail="Denfe não encontrado")
    return db_danfe

@router.delete("/{id_danfe}", status_code=204)
async def excluir_danfe(id_danfe: int, db: AsyncSession = Depends(get_session)):
    db_danfe = await delete_danfe(db, id_danfe)
    if not db_danfe:
        raise HTTPException(status_code=404, detail="Danfe não encontrado")
    return {"ok": True, "message": "Danfe excluído com sucesso"}
