from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schema.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate, SingleResponse, PaginatedResponse
from app.database.session import get_session
from app.core.pagination import DEFAULT_PAGE
from app.service import contribuinte_service
from app.core.exceptions import DuplicateEntryError, DatabaseError


router = APIRouter(prefix="/contribuinte", tags=["Contribuinte"])

@router.get("/", response_model=PaginatedResponse)
async def get_contribuintes(page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.get_contribuintes(page=page, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/danfe-endereco", response_model=PaginatedResponse)
async def get_contribuintes_danfe_endereco(filtro_nome: str, page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.get_contribuintes_danfe_endereco(filtro_nome=filtro_nome, page=page, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/cd", response_model=SingleResponse)
async def get_contribuinte_por_cd(cd_contribuinte: str, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.get_contribuinte_por_cd(cd_contribuinte=cd_contribuinte, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/cnpj", response_model=SingleResponse)
async def get_contribuinte_por_cnpj(cnpj_contribuinte: str, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.get_contribuinte_por_cnpj(cnpj_contribuinte=cnpj_contribuinte, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=SingleResponse, status_code=201)
async def create_contribuinte(contribuinte: ContribuinteCreate, db: AsyncSession = Depends(get_session)):
    try:
        return await contribuinte_service.create_contribuinte(contribuinte=contribuinte, db=db)
    except DuplicateEntryError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{cd_contribuinte}", response_model=SingleResponse)
async def update_contribuinte(cd_contribuinte: str, contribuinte: ContribuinteUpdate, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.update_contribuinte(cd_contribuinte=cd_contribuinte, contribuinte=contribuinte, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{cd_contribuinte}", status_code=204)
async def delete_contribuinte(cd_contribuinte: str, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.delete_contribuinte(cd_contribuinte=cd_contribuinte, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return {"ok": True, "message": "Contribuinte excluído com sucesso"}
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
