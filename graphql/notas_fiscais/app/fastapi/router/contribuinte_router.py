from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.contribuinte_schema import Contribuinte, ContribuinteCreate, ContribuinteUpdate
from app.fastapi.validators.contribuinte_validator import CD_CONTRIBUINTE_PATH
from app.model.contribuinte_model import ContribuinteModel
from app.service.contribuinte_service import ContribuinteService
from app.fastapi.utils.exception_util import raise_http_exception
from app.fastapi.utils.field_util import parse_fields_param, select_fields_from_obj
from app.fastapi.utils.response_util import normalize_pagination_params, set_filters_params, set_order_params, set_pagination_headers


router = APIRouter(prefix="/v1/contribuinte", tags=["Contribuinte"])

@router.get("/")
async def get_list(
    request: Request,
    response: Response,
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    fields: Optional[str] = Query(None),
    session: AsyncSession = Depends(get_session)
):
    try:
        # Monta filtros, ordenação e normaliza parâmetros
        filters = set_filters_params(request=request)
        order = set_order_params(request=request, model=ContribuinteModel)
        final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

        # Chama o service passando os valores normalizados
        service = ContribuinteService(session=session)
        total, items = await service.get_list(filters=filters, order=order, offset=final_offset, limit=final_limit)

        # Aplica headers
        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        # Transformação de campos
        requested_fields = parse_fields_param(fields)
        transformed = [select_fields_from_obj(i, requested_fields) for i in items]

        return transformed
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/{cd_contribuinte}", response_model=Contribuinte)
async def get_by_cd(cd_contribuinte: str = CD_CONTRIBUINTE_PATH, session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.get_by_cd(cd=cd_contribuinte)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return result


@router.post("/", response_model=Contribuinte, status_code=201)
async def create(contribuinte: ContribuinteCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.create(contribuinte.model_dump())
        return result
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{cd_contribuinte}", response_model=Contribuinte)
async def update(cd_contribuinte: str = CD_CONTRIBUINTE_PATH, contribuinte: ContribuinteUpdate = ..., session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.update(cd_contribuinte, contribuinte.model_dump(exclude_unset=True))
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return result


@router.delete("/{cd_contribuinte}", status_code=204)
async def delete(cd_contribuinte: str = CD_CONTRIBUINTE_PATH, session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.delete(cd_contribuinte)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return Response(status_code=204)
