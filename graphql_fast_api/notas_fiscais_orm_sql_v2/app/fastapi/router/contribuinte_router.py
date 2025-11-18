from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schema.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate, SingleResponse, PaginatedResponse
from app.database.session import get_session
from app.core.pagination import DEFAULT_PAGE
from app.service import contribuinte_service
from app.core.exceptions import DuplicateEntryError, DatabaseError


router = APIRouter(prefix="/contribuinte", tags=["Contribuinte"])

@router.get("/danfe-endereco", response_model=PaginatedResponse)
async def listar_contribuintes_danfe_endereco(filtro_nome: str, page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    result = await contribuinte_service.get_contribuintes_danfe_endereco(filtro_nome, page, db)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/", response_model=PaginatedResponse)
async def get_contribuintes(page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    result = await contribuinte_service.get_contribuintes(page, db)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/cd", response_model=SingleResponse)
async def get_contribuinte_por_cd(cd_contribuinte: str, db: AsyncSession = Depends(get_session)):
    result = await contribuinte_service.get_contribuinte_por_cd(cd_contribuinte, db)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.get("/cnpj", response_model=SingleResponse)
async def get_contribuinte_por_cnpj(cnpj_contribuinte: str, db: AsyncSession = Depends(get_session)):
    result = await contribuinte_service.get_contribuinte_por_cnpj(cnpj_contribuinte, db)
    if not result["data"]:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    return result


@router.post("/", response_model=SingleResponse, status_code=201)
async def criar_contribuinte(contribuinte: ContribuinteCreate, db: AsyncSession = Depends(get_session)):
    try:
        return await contribuinte_service.create_contribuinte(contribuinte, db)
    except DuplicateEntryError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{cd_contribuinte}", response_model=SingleResponse)
async def atualizar_contribuinte(cd_contribuinte: str, updates: ContribuinteUpdate, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.update_contribuinte(cd_contribuinte, updates, db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.delete("/{cd_contribuinte}", status_code=204)
async def excluir_contribuinte(cd_contribuinte: str, db: AsyncSession = Depends(get_session)):
    try:
        result = await contribuinte_service.delete_contribuinte(cd_contribuinte, db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
        return {"ok": True, "message": "Contribuinte excluído com sucesso"}
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
