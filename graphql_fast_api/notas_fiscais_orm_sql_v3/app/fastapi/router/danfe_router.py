from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schema.danfe_schema import  DanfeCreate, DanfeUpdate, SingleResponse, PaginatedResponse
from app.database.session import get_session
from app.core.pagination import DEFAULT_PAGE
from app.service import danfe_service
from app.core.exceptions import DuplicateEntryError, DatabaseError


router = APIRouter(prefix="/danfe", tags=["Danfe"])

@router.get("/", response_model=PaginatedResponse)
async def get_danfes(page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    try:
        result = await danfe_service.get_danfes(page=page, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Danfe não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id_danfe}", response_model=SingleResponse)
async def get_danfe(id_danfe: int, db: AsyncSession = Depends(get_session)):
    try:
        result = await danfe_service.get_danfe(id_danfe=id_danfe, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Danfe não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=SingleResponse, status_code=201)
async def create_danfe(danfe: DanfeCreate, db: AsyncSession = Depends(get_session)):
    try:
        return await danfe_service.create_danfe(danfe=danfe, db=db)
    except DuplicateEntryError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{id_danfe}", response_model=SingleResponse)
async def update_danfe(id_danfe: int, danfe: DanfeUpdate, db: AsyncSession = Depends(get_session)):
    try:
        result = await danfe_service.update_danfe(id_danfe=id_danfe, danfe=danfe, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Denfe não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id_danfe}", status_code=204)
async def delete_danfe(id_danfe: int, db: AsyncSession = Depends(get_session)):
    try:
        result = await danfe_service.delete_danfe(id_danfe=id_danfe, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Danfe não encontrado")
        return {"ok": True, "message": "Danfe excluído com sucesso"}
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
