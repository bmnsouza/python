from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.danfe_schema import Danfe, DanfeCreate, DanfeUpdate
from app.fastapi.validators.danfe_validator import ID_DANFE_PATH
from app.service.danfe_service import DanfeService
from app.utils.exception_util import raise_http_exception
from app.utils.field_util import parse_fields_param, select_fields_from_obj
from app.utils.response_util import normalize_pagination_params, set_filters_order, set_pagination_headers


router = APIRouter(prefix="/v1/danfe", tags=["Danfe"])

@router.get("/")
async def get_list(request: Request, response: Response, asc: Optional[str] = Query(None), des: Optional[str] = Query(None),
    offset: int = Query(None, ge=0), limit: int = Query(None, ge=1), fields: Optional[str] = Query(None), session: AsyncSession = Depends(get_session)):
    # Normaliza parâmetros antes de chamar o service
    final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

    # Monta filtros e ordenação
    filters, order = set_filters_order(request=request, asc=asc, des=des)

    try:
        # Chama o service passando os valores normalizados
        service = DanfeService(session)
        total, items = await service.get_list(filters=filters, order=order, offset=final_offset, limit=final_limit)
    except Exception as e:
        raise_http_exception(exc=e)

    # Aplica headers
    set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

    # Transformação de campos
    requested_fields = parse_fields_param(fields)
    transformed = [select_fields_from_obj(i, requested_fields) for i in items]

    return transformed


@router.get("/{id_danfe}", response_model=Danfe)
async def get_by_id(id_danfe: str = ID_DANFE_PATH, session: AsyncSession = Depends(get_session)):
    try:
        service = DanfeService(session)
        result = await service.get_by_id(id_danfe)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Danfe não encontrado")

    return result


@router.post("/", response_model=Danfe, status_code=201)
async def create(danfe: DanfeCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = DanfeService(session)
        result = await service.create(danfe.model_dump())
        return result
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{id_danfe}", response_model=Danfe)
async def update(id_danfe: str = ID_DANFE_PATH, danfe: DanfeUpdate = ..., session: AsyncSession = Depends(get_session)):
    try:
        service = DanfeService(session)
        result = await service.update(id_danfe, danfe.model_dump(exclude_unset=True))
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Danfe não encontrado")

    return result


@router.delete("/{id_danfe}", status_code=204)
async def delete(id_danfe: str = ID_DANFE_PATH, session: AsyncSession = Depends(get_session)):
    try:
        service = DanfeService(session)
        result = await service.delete(id_danfe)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Danfe não encontrado")

    return Response(status_code=204)
