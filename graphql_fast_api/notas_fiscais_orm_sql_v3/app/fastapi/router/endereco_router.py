from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.fastapi.schema.endereco_schema import EnderecoCreate, EnderecoUpdate, SingleResponse, PaginatedResponse
from app.database.session import get_session
from app.core.pagination import DEFAULT_PAGE
from app.service import endereco_service
from app.core.exceptions import DuplicateEntryError, DatabaseError


router = APIRouter(prefix="/endereco", tags=["Endereço"])

@router.get("/", response_model=PaginatedResponse)
async def get_enderecos(page: int = DEFAULT_PAGE, db: AsyncSession = Depends(get_session)):
    try:
        result = await endereco_service.get_enderecos(page=page, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Endereço não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{id_endereco}", response_model=SingleResponse)
async def get_endereco(id_endereco: int, db: AsyncSession = Depends(get_session)):
    try:
        result = await endereco_service.get_endereco(id_endereco=id_endereco, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Endereço não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/", response_model=SingleResponse, status_code=201)
async def create_endereco(endereco: EnderecoCreate, db: AsyncSession = Depends(get_session)):
    try:
        return await endereco_service.create_endereco(endereco=endereco, db=db)
    except DuplicateEntryError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{id_endereco}", response_model=SingleResponse)
async def update_endereco(id_endereco: int, endereco: EnderecoUpdate, db: AsyncSession = Depends(get_session)):
    try:
        result = await endereco_service.update_endereco(id_endereco=id_endereco, endereco=endereco, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Endereço não encontrado")
        return result
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{id_endereco}", status_code=204)
async def delete_endereco(id_endereco: int, db: AsyncSession = Depends(get_session)):
    try:
        result = await endereco_service.delete_endereco(id_endereco=id_endereco, db=db)
        if not result["data"]:
            raise HTTPException(status_code=404, detail="Endereço não encontrado")
        return {"ok": True, "message": "Endereço excluído com sucesso"}
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
