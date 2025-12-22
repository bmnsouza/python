from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.contribuinte_schema import Contribuinte, ContribuinteCreate, ContribuinteUpdate
from app.fastapi.utils.exception_util import raise_http_exception
from app.fastapi.utils.field_util import parse_fields_param, select_fields_from_obj, validate_fields_param
from app.fastapi.utils.response_util import get_contribuinte_filters, normalize_pagination_params, set_filters_params, set_order_params, set_pagination_headers
from app.fastapi.validator.contribuinte_validator import ContribuintePath
from app.model.contribuinte_model import ContribuinteModel
from app.service.contribuinte_service import ContribuinteService


router = APIRouter(prefix="/v1/contribuinte", tags=["Contribuinte"])

# @router.get("/")
# async def get_list(
#     request: Request,
#     response: Response,
#     offset: int = Query(None, ge=0),
#     limit: int = Query(None, ge=1),
#     fields: Optional[str] = Query(None),
#     session: AsyncSession = Depends(get_session)
# ):
#     try:
#         # Monta filtros, ordenação e normaliza parâmetros
#         filters = set_filters_params(request=request)
#         order = set_order_params(request=request, model=ContribuinteModel)
#         final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

#         # Chama o service passando os valores normalizados
#         service = ContribuinteService(session=session)
#         total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

#         # Aplica headers
#         set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

#         # Transformação de campos
#         requested_fields = parse_fields_param(fields)
#         transformed = [select_fields_from_obj(i, requested_fields) for i in items]

#         return transformed
#     except Exception as e:
#         raise_http_exception(exc=e)


@router.get("/")
async def get_list(
    request: Request,
    response: Response,
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    fields: Optional[str] = Query(None),
    filters: dict = Depends(get_contribuinte_filters),
    session: AsyncSession = Depends(get_session)
):
    try:
        # Monta filtros, ordenação e normaliza parâmetros
        order = set_order_params(request=request, model=ContribuinteModel)
        final_offset, final_limit, final_accept_ranges = normalize_pagination_params(offset=offset, limit=limit)

        # Chama o service passando os valores normalizados
        service = ContribuinteService(session=session)
        total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

        # Aplica headers
        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        # Transformação de campos
        requested_fields = validate_fields_param(fields, ContribuinteModel)
        transformed = [select_fields_from_obj(i, requested_fields) for i in items]

        return transformed
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/sql")
async def get_list_sql(
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
        total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=filters, order=order)

        # Aplica headers
        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        # Transformação de campos
        requested_fields = parse_fields_param(fields)
        transformed = [select_fields_from_obj(i, requested_fields) for i in items]

        return transformed
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/{cd_contribuinte}", response_model=Contribuinte)
async def get_by_cd(path: ContribuintePath = Depends(), session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.get_by_cd(cd=path.cd_contribuinte)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return result


@router.post("/", response_model=Contribuinte, status_code=201)
async def create(contribuinte: ContribuinteCreate, session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.create(data=contribuinte.model_dump())
        return result
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{cd_contribuinte}", response_model=Contribuinte)
async def update(path: ContribuintePath = Depends(), contribuinte: ContribuinteUpdate = ..., session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.update(cd=path.cd_contribuinte, data=contribuinte.model_dump(exclude_unset=True))
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return result


@router.delete("/{cd_contribuinte}", status_code=204)
async def delete(path: ContribuintePath = Depends(), session: AsyncSession = Depends(get_session)):
    try:
        service = ContribuinteService(session=session)
        result = await service.delete(cd=path.cd_contribuinte)
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Contribuinte não encontrado")
