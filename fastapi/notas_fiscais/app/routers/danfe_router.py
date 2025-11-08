from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud.danfe_crud import get_danfes, get_danfe, create_danfe, update_danfe, delete_danfe
from app.database import get_db
from app.schemas import danfe_schema

router = APIRouter(prefix="/danfe", tags=["Danfe"])

@router.get("/", response_model=List[danfe_schema.Danfe])
def listar_danfes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_danfes(db, skip=skip, limit=limit)

@router.get("/{id_danfe}", response_model=danfe_schema.Danfe)
def obter_danfe(id_danfe: int, db: Session = Depends(get_db)):
    db_danfe = get_danfe(db, id_danfe)
    if not db_danfe:
        raise HTTPException(status_code=404, detail="DANFE não encontrado")
    return db_danfe

@router.post("/", response_model=danfe_schema.Danfe, status_code=201)
def criar_danfe(danfe: danfe_schema.DanfeCreate, db: Session = Depends(get_db)):
    return create_danfe(db, danfe)

@router.put("/{id_danfe}", response_model=danfe_schema.Danfe)
def atualizar_danfe(id_danfe: int, updates: danfe_schema.DanfeUpdate, db: Session = Depends(get_db)):
    db_danfe = update_danfe(db, id_danfe, updates)
    if not db_danfe:
        raise HTTPException(status_code=404, detail="DANFE não encontrado")
    return db_danfe

@router.delete("/{id_danfe}", status_code=204)
def excluir_danfe(id_danfe: int, db: Session = Depends(get_db)):
    db_danfe = delete_danfe(db, id_danfe)
    if not db_danfe:
        raise HTTPException(status_code=404, detail="DANFE não encontrado")
    return {}
