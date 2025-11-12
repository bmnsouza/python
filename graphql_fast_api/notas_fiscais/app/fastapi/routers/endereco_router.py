from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schemas.endereco_schema import Endereco, EnderecoCreate, EnderecoUpdate
from app.database import get_session
from app.crud.endereco_crud import get_enderecos, get_endereco, create_endereco, update_endereco, delete_endereco

router = APIRouter(prefix="/endereco", tags=["Endereço"])

@router.get("/", response_model=List[Endereco])
async def listar_enderecos(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    return await get_enderecos(db, skip=skip, limit=limit)

@router.get("/{id_endereco}", response_model=Endereco)
async def obter_endereco(id_endereco: int, db: AsyncSession = Depends(get_session)):
    db_endereco = await get_endereco(db, id_endereco)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco

@router.post("/", response_model=Endereco, status_code=201)
async def criar_endereco(endereco: EnderecoCreate, db: AsyncSession = Depends(get_session)):
    return await create_endereco(db, endereco)

@router.put("/{id_endereco}", response_model=Endereco)
async def atualizar_endereco(id_endereco: int, updates: EnderecoUpdate, db: AsyncSession = Depends(get_session)):
    db_endereco = await update_endereco(db, id_endereco, updates)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco

@router.delete("/{id_endereco}", status_code=204)
async def excluir_endereco(id_endereco: int, db: AsyncSession = Depends(get_session)):
    db_endereco = await delete_endereco(db, id_endereco)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return {"ok": True, "message": "Endereço excluído com sucesso"}
