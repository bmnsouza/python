from typing import Dict, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.contribuinte_schema import Contribuinte, ContribuinteCreate, ContribuinteUpdate
from app.service.contribuinte_service import ContribuinteService
from app.utils.exception_utils import raise_http_exception
from app.utils.response_utils import build_order_by_clause, parse_fields_param, select_fields_from_obj, set_pagination_headers

from app.fastapi.validators.contribuinte_validators import CD_CONTRIBUINTE_PATH


router = APIRouter(prefix="/v1/contribuinte", tags=["Contribuinte"])

@router.get("/")
async def get_list(
    request: Request,
    response: Response,
    asc: Optional[str] = Query(None),
    des: Optional[str] = Query(None),
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=1),
    fields: Optional[str] = Query(None),
    accept_ranges: Optional[int] = Query(None),
    session: AsyncSession = Depends(get_session)
):
    # Filtros dinâmicos
    raw_params: Dict[str, str] = dict(request.query_params)
    reserved = {"asc", "des", "offset", "limit", "fields", "accept_ranges"}
    filters = {k: v for k, v in raw_params.items() if k not in reserved}

    order = build_order_by_clause(asc, des)

    try:
        service = ContribuinteService(session)
        total, items = await service.get_list(filters=filters, order=order, offset=offset, limit=limit)
    except Exception as e:
        raise_http_exception(exc=e)

    requested_fields = parse_fields_param(fields)
    transformed = [select_fields_from_obj(i, requested_fields) for i in items]

    set_pagination_headers(response, offset, limit, total, accept_ranges)
    return transformed


@router.get("/{cd_contribuinte}", response_model=Contribuinte)
async def get_by_cd(
    cd_contribuinte: str = CD_CONTRIBUINTE_PATH,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = ContribuinteService(session)
        result = await service.get_by_cd(cd_contribuinte)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return result


@router.post("/", response_model=Contribuinte, status_code=201)
async def create(contribuinte: ContribuinteCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session)
        result = await service.create(contribuinte.model_dump())
        return result
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{cd_contribuinte}", response_model=Contribuinte)
async def update(
    cd_contribuinte: str = CD_CONTRIBUINTE_PATH,
    contribuinte: ContribuinteUpdate = ...,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = ContribuinteService(session)
        result = await service.update(
            cd_contribuinte,
            contribuinte.model_dump(exclude_unset=True),
        )
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return result


@router.delete("/{cd_contribuinte}", status_code=204)
async def delete(
    cd_contribuinte: str = CD_CONTRIBUINTE_PATH,
    session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session)
        result = await service.delete(cd_contribuinte)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return Response(status_code=204)
