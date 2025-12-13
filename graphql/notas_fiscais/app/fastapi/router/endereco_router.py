from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.endereco_schema import Endereco, EnderecoCreate, EnderecoUpdate
from app.fastapi.validators.endereco_validator import ID_ENDERECO_PATH
from app.model.endereco_model import EnderecoModel
from app.service.endereco_service import EnderecoService
from app.utils.exception_util import raise_http_exception
from app.utils.field_util import parse_fields_param, select_fields_from_obj
from app.utils.response_util import normalize_pagination_params, set_filters_params, set_order_params, set_pagination_headers


router = APIRouter(prefix="/v1/endereco", tags=["Endereco"])

@router.get("/")
async def get_list(request: Request, response: Response, offset: int = Query(None, ge=0), limit: int = Query(None, ge=1), fields: Optional[str] = Query(None), session: AsyncSession = Depends(get_session)):
    # Monta filtros, ordenação e normaliza parâmetros
    filters = set_filters_params(request=request)
    order = set_order_params(request=request, model=EnderecoModel)
    final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

    try:
        # Chama o service passando os valores normalizados
        service = EnderecoService(session=session)
        total, items = await service.get_list(filters=filters, order=order, offset=final_offset, limit=final_limit)
    except Exception as e:
        raise_http_exception(exc=e)

    # Aplica headers
    set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

    # Transformação de campos
    requested_fields = parse_fields_param(fields)
    transformed = [select_fields_from_obj(i, requested_fields) for i in items]

    return transformed


@router.get("/{id_endereco}", response_model=Endereco)
async def get_by_id(id_endereco: str = ID_ENDERECO_PATH, session: AsyncSession = Depends(get_session)):
    try:
        service = EnderecoService(session=session)
        result = await service.get_by_id(id_endereco)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    return result


@router.post("/", response_model=Endereco, status_code=201)
async def create(endereco: EnderecoCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = EnderecoService(session=session)
        result = await service.create(endereco.model_dump())
        return result
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{id_endereco}", response_model=Endereco)
async def update(id_endereco: str = ID_ENDERECO_PATH, endereco: EnderecoUpdate = ..., session: AsyncSession = Depends(get_session)):
    try:
        service = EnderecoService(session=session)
        result = await service.update(id_endereco, endereco.model_dump(exclude_unset=True))
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    return result


@router.delete("/{id_endereco}", status_code=204)
async def delete(id_endereco: str = ID_ENDERECO_PATH, session: AsyncSession = Depends(get_session)):
    try:
        service = EnderecoService(session=session)
        result = await service.delete(id_endereco)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    return Response(status_code=204)
