from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud.contribuinte_crud import get_contribuintes, get_contribuinte, create_contribuinte, update_contribuinte, delete_contribuinte
from app.database import get_db
from app.schemas import contribuinte_schema

router = APIRouter(prefix="/contribuinte", tags=["Contribuinte"])

@router.get("/", response_model=List[contribuinte_schema.Contribuinte])
def listar_contribuintes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_contribuintes(db, skip=skip, limit=limit)

@router.get("/{cd_contribuinte}", response_model=contribuinte_schema.Contribuinte)
def obter_contribuinte(cd_contribuinte: str, db: Session = Depends(get_db)):
    db_contribuinte = get_contribuinte(db, cd_contribuinte)
    if not db_contribuinte:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return db_contribuinte

@router.post("/", response_model=contribuinte_schema.Contribuinte, status_code=201)
def criar_contribuinte(contribuinte: contribuinte_schema.ContribuinteCreate, db: Session = Depends(get_db)):
    return create_contribuinte(db, contribuinte)

@router.put("/{cd_contribuinte}", response_model=contribuinte_schema.Contribuinte)
def atualizar_contribuinte(cd_contribuinte: str, updates: contribuinte_schema.ContribuinteUpdate, db: Session = Depends(get_db)):
    db_contribuinte = update_contribuinte(db, cd_contribuinte, updates)
    if not db_contribuinte:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return db_contribuinte

@router.delete("/{cd_contribuinte}", status_code=204)
def excluir_contribuinte(cd_contribuinte: str, db: Session = Depends(get_db)):
    db_contribuinte = delete_contribuinte(db, cd_contribuinte)
    if not db_contribuinte:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return {}
