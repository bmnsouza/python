from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exception.rest_exception import raise_http_exception
from app.core.response.rest_response import set_filters_params, set_order_params, set_pagination_params, set_pagination_headers, validate_fields_param, select_fields_from_obj
from app.database.session import get_session
from app.schema.danfe_schema import Danfe, DanfeCreate, DanfeItem, DanfeUpdate
from app.model.danfe_model import DanfeModel
from app.service.danfe_service import DanfeService
from app.validator.danfe_validator import DanfeLastSevenDaysParam, DanfeParams, DanfeParam


router = APIRouter(prefix="/v1/danfe", tags=["Danfe"])

@router.get("/")
async def get_list(
    request: Request,
    response: Response,
    params: DanfeParams = Depends(),
    fields: Optional[str] = Query(None),
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    session: AsyncSession = Depends(get_session)
):
    try:
        params = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, model=DanfeModel)
        order = set_order_params(request=request, schema=DanfeItem)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        service = DanfeService(session=session)
        total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=params, order=order)

        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        result = [select_fields_from_obj(i, requested_fields) for i in items]
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/sql")
async def get_list_sql(
    request: Request,
    response: Response,
    params: DanfeParams = Depends(),
    fields: Optional[str] = Query(None),
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    session: AsyncSession = Depends(get_session)
):
    try:
        params = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, schema=DanfeItem)
        order = set_order_params(request=request, schema=DanfeItem)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        service = DanfeService(session=session)
        total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=params, order=order)

        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        result = [select_fields_from_obj(i, requested_fields) for i in items]
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/last-seven-days-sql/{cd_contribuinte}")
async def get_last_seven_days_sql(
    request: Request,
    response: Response,
    param: DanfeLastSevenDaysParam = Depends(),
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    session: AsyncSession = Depends(get_session)
):
    try:
        set_filters_params(request=request, params=param, allow_order=False, allow_fields=False)

        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        service = DanfeService(session=session)
        total, items = await service.get_last_seven_days_sql(offset=final_offset, limit=final_limit, cd_contribuinte=param.cd_contribuinte)

        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        return items
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/{id_danfe}", response_model=DanfeItem)
async def get_by_id(
    param: DanfeParam = Depends(),
    session: AsyncSession = Depends(get_session)
):
    try:
        service = DanfeService(session=session)
        result = await service.get_by_id(id=param.id_danfe)

        if not result:
            raise HTTPException(status_code=404, detail="Danfe não encontrado")

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.post("/", response_model=Danfe, status_code=201)
async def create(
    danfe: DanfeCreate,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = DanfeService(session=session)
        result = await service.create(danfe.model_dump())
        return result
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{id_danfe}", response_model=Danfe)
async def update(
    param: DanfeParam = Depends(),
    danfe: DanfeUpdate = ...,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = DanfeService(session=session)
        result = await service.update(id=param.id_danfe, data=danfe.model_dump(exclude_unset=True))

        if not result:
            raise HTTPException(status_code=404, detail="Danfe não encontrado")

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.delete("/{id_danfe}", status_code=204)
async def delete(
    param: DanfeParam = Depends(),
    session: AsyncSession = Depends(get_session)
):
    try:
        service = DanfeService(session=session)
        result = await service.delete(id=param.id_danfe)

        if not result:
            raise HTTPException(status_code=404, detail="Danfe não encontrado")
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)
