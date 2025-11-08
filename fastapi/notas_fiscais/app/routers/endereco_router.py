from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud.endereco_crud import get_enderecos, get_endereco, create_endereco, update_endereco, delete_endereco
from app.database import get_db
from app.schemas import endereco_schema

router = APIRouter(prefix="/endereco", tags=["Endereço"])

@router.get("/", response_model=List[endereco_schema.Endereco])
def listar_enderecos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_enderecos(db, skip=skip, limit=limit)

@router.get("/{id_endereco}", response_model=endereco_schema.Endereco)
def obter_endereco(id_endereco: int, db: Session = Depends(get_db)):
    db_endereco = get_endereco(db, id_endereco)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco

@router.post("/", response_model=endereco_schema.Endereco, status_code=201)
def criar_endereco(endereco: endereco_schema.EnderecoCreate, db: Session = Depends(get_db)):
    return create_endereco(db, endereco)

@router.put("/{id_endereco}", response_model=endereco_schema.Endereco)
def atualizar_endereco(id_endereco: int, updates: endereco_schema.EnderecoUpdate, db: Session = Depends(get_db)):
    db_endereco = update_endereco(db, id_endereco, updates)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco

@router.delete("/{id_endereco}", status_code=204)
def excluir_endereco(id_endereco: int, db: Session = Depends(get_db)):
    db_endereco = delete_endereco(db, id_endereco)
    if not db_endereco:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return {}
