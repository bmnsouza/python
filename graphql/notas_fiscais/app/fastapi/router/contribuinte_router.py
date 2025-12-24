from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.contribuinte_schema import Contribuinte, ContribuinteCreate, ContribuinteListItem, ContribuinteUpdate
from app.fastapi.utils.exception_util import raise_http_exception
from app.fastapi.utils.field_util import select_fields_from_obj, validate_fields_param
from app.fastapi.utils.response_util import set_filters_params, set_order_params, set_pagination_params, set_pagination_headers
from app.model.contribuinte_model import ContribuinteModel
from app.service.contribuinte_service import ContribuinteService
from app.validator.contribuinte_validator import ContribuinteParams, ContribuinteParam


router = APIRouter(prefix="/v1/contribuinte", tags=["Contribuinte"])

@router.get("/")
async def get_list(
    request: Request,
    response: Response,
    params: ContribuinteParams = Depends(),
    fields: Optional[str] = Query(None),
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    session: AsyncSession = Depends(get_session)
):
    try:
        params = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, orm_model=ContribuinteModel)
        order = set_order_params(request=request, orm_model=ContribuinteModel)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        service = ContribuinteService(session=session)
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
    params: ContribuinteParams = Depends(),
    fields: Optional[str] = Query(None),
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    session: AsyncSession = Depends(get_session)
):
    try:
        params = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, schema=ContribuinteListItem)
        order = set_order_params(request=request, schema=ContribuinteListItem)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        service = ContribuinteService(session=session)
        total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=params, order=order)

        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        result = [select_fields_from_obj(i, requested_fields) for i in items]
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/{cd_contribuinte}", response_model=Contribuinte)
async def get_by_cd(
    param: ContribuinteParam = Depends(),
    session: AsyncSession = Depends(get_session)
):
    try:
        service = ContribuinteService(session=session)
        result = await service.get_by_cd(cd=param.cd_contribuinte)

        if not result:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.post("/", response_model=Contribuinte, status_code=201)
async def create(
    contribuinte: ContribuinteCreate,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = ContribuinteService(session=session)
        result = await service.create(data=contribuinte.model_dump())
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{cd_contribuinte}", response_model=Contribuinte)
async def update(
    param: ContribuinteParam = Depends(),
    contribuinte: ContribuinteUpdate = ...,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = ContribuinteService(session=session)
        result = await service.update(cd=param.cd_contribuinte, data=contribuinte.model_dump(exclude_unset=True))

        if not result:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.delete("/{cd_contribuinte}", status_code=204)
async def delete(
    param: ContribuinteParam = Depends(),
    session: AsyncSession = Depends(get_session)
):
    try:
        service = ContribuinteService(session=session)
        result = await service.delete(cd=param.cd_contribuinte)

        if not result:
            raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)
