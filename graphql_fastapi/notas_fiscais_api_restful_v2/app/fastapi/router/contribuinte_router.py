# app/router/contribuinte_router.py
from typing import Optional, Dict, List
from fastapi import APIRouter, Depends, Request, Response, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_session
from app.service.contribuinte_service import ContribuinteService
from app.utils.response_utils import (
    parse_fields_param,
    select_fields_from_obj,
    build_order_by_clause,
    set_pagination_headers,
)
from app.fastapi.schema.contribuinte_schema import (
    ContribuinteCreate,
    ContribuinteUpdate,
    SingleResponse,
)
from app.utils.error_utils import map_data_base_error

router = APIRouter(prefix="/v1/contribuinte", tags=["Contribuinte"])


def format_exception(description: str, code="server_error", title="Internal Server Error"):
    return {"errors": [{"code": code, "title": title, "description": description}]}


@router.get("", response_model=List[dict])
async def get_contribuinte_list(
    request: Request,
    response: Response,
    asc: Optional[str] = Query(None),
    des: Optional[str] = Query(None),
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=1),
    fields: Optional[str] = Query(None),
    accept_ranges: Optional[int] = Query(None),
    session: AsyncSession = Depends(get_session),
):

    # filtros dinâmicos
    raw_params: Dict[str, str] = dict(request.query_params)
    reserved = {"asc", "des", "offset", "limit", "fields", "accept_ranges"}
    filters = {k: v for k, v in raw_params.items() if k not in reserved}

    order = build_order_by_clause(asc, des)

    try:
        service = ContribuinteService(session)
        total, items = await service.list_contribuintes(
            filters=filters, order=order, offset=offset, limit=limit
        )
    except Exception as e:
        map_data_base_error(e)
        raise HTTPException(status_code=500, detail=format_exception(str(e)))

    requested_fields = parse_fields_param(fields)
    transformed = [select_fields_from_obj(i, requested_fields) for i in items]

    set_pagination_headers(response, offset, limit, total, accept_ranges)
    return transformed


@router.get("/cd", response_model=SingleResponse)
async def get_contribuinte_por_cd(
    cd_contribuinte: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        service = ContribuinteService(session)
        result = await service.get_contribuinte_por_cd(cd_contribuinte)
    except Exception as e:
        map_data_base_error(e)
        raise HTTPException(status_code=500, detail=format_exception(str(e)))

    if not result:
        raise HTTPException(
            status_code=404,
            detail={"errors": [{"code": "not_found", "title": "Not Found", "description": "Contribuinte não encontrado"}]},
        )

    return {"data": result}


@router.get("/cnpj", response_model=SingleResponse)
async def get_contribuinte_por_cnpj(
    cnpj_contribuinte: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        service = ContribuinteService(session)
        result = await service.get_contribuinte_por_cnpj(cnpj_contribuinte)
    except Exception as e:
        map_data_base_error(e)
        raise HTTPException(status_code=500, detail=format_exception(str(e)))

    if not result:
        raise HTTPException(
            status_code=404,
            detail={"errors": [{"code": "not_found", "title": "Not Found", "description": "Contribuinte não encontrado"}]},
        )

    return {"data": result}


@router.post("/", response_model=SingleResponse, status_code=201)
async def create_contribuinte(
    contribuinte: ContribuinteCreate,
    session: AsyncSession = Depends(get_session),
):
    try:
        service = ContribuinteService(session)
        result = await service.create_contribuinte(contribuinte.model_dump())
        return {"data": result}
    except Exception as e:
        map_data_base_error(e)
        raise HTTPException(status_code=500, detail=format_exception(str(e)))


@router.put("/{cd_contribuinte}", response_model=SingleResponse)
async def update_contribuinte(
    cd_contribuinte: str,
    contribuinte: ContribuinteUpdate,
    session: AsyncSession = Depends(get_session),
):
    try:
        service = ContribuinteService(session)
        result = await service.update_contribuinte(
            cd_contribuinte,
            contribuinte.model_dump(exclude_unset=True),
        )
    except Exception as e:
        map_data_base_error(e)
        raise HTTPException(status_code=500, detail=format_exception(str(e)))

    if not result:
        raise HTTPException(
            status_code=404,
            detail={"errors": [{"code": "not_found", "title": "Not Found", "description": "Contribuinte não encontrado"}]},
        )

    return {"data": result}


@router.delete("/{cd_contribuinte}", status_code=204)
async def delete_contribuinte(
    cd_contribuinte: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        service = ContribuinteService(session)
        result = await service.delete_contribuinte(cd_contribuinte)
    except Exception as e:
        map_data_base_error(e)
        raise HTTPException(status_code=500, detail=format_exception(str(e)))

    if not result:
        raise HTTPException(
            status_code=404,
            detail={"errors": [{"code": "not_found", "title": "Not Found", "description": "Contribuinte não encontrado"}]},
        )

    return Response(status_code=204)
