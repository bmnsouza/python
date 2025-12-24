from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.endereco_schema import Endereco, EnderecoCreate, EnderecoUpdate
from app.fastapi.utils.exception_util import raise_http_exception
from app.fastapi.utils.field_util import validate_fields_param, select_fields_from_obj
from app.fastapi.utils.response_util import set_filters_params, set_order_params, set_pagination_params, set_pagination_headers
from app.model.endereco_model import EnderecoModel
from app.service.endereco_service import EnderecoService
from app.validator.endereco_validator import EnderecoParams, EnderecoParam


router = APIRouter(prefix="/v1/endereco", tags=["Endereco"])

@router.get("/")
async def get_list(
    request: Request,
    response: Response,
    params: EnderecoParams = Depends(),
    fields: Optional[str] = Query(None),
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    session: AsyncSession = Depends(get_session)
):
    try:
        params = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, model=EnderecoModel)
        order = set_order_params(request=request, model=EnderecoModel)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        service = EnderecoService(session=session)
        total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=params, order=order)

        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        transformed = [select_fields_from_obj(i, requested_fields) for i in items]
        return transformed
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/sql")
async def get_list_sql(
    request: Request,
    response: Response,
    params: EnderecoParams = Depends(),
    fields: Optional[str] = Query(None),
    offset: int = Query(None, ge=0),
    limit: int = Query(None, ge=1),
    session: AsyncSession = Depends(get_session)
):
    try:
        params = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, model=EnderecoModel)
        order = set_order_params(request=request, model=EnderecoModel)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        service = EnderecoService(session=session)
        total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=params, order=order)

        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        transformed = [select_fields_from_obj(i, requested_fields) for i in items]
        return transformed
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/{id_endereco}", response_model=Endereco)
async def get_by_id(
    param: EnderecoParam = Depends(),
    session: AsyncSession = Depends(get_session)
):
    try:
        service = EnderecoService(session=session)
        result = await service.get_by_id(id=param.id_endereco)

        if not result:
            raise HTTPException(status_code=404, detail="Endereço não encontrado")

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.post("/", response_model=Endereco, status_code=201)
async def create(
    endereco: EnderecoCreate,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = EnderecoService(session=session)
        result = await service.create(endereco.model_dump())
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{id_endereco}", response_model=Endereco)
async def update(
    param: EnderecoParam = Depends(),
    endereco: EnderecoUpdate = ...,
    session: AsyncSession = Depends(get_session)
):
    try:
        service = EnderecoService(session=session)
        result = await service.update(id=param.id_endereco, data=endereco.model_dump(exclude_unset=True))

        if not result:
            raise HTTPException(status_code=404, detail="Endereço não encontrado")

        return result
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.delete("/{id_endereco}", status_code=204)
async def delete(
    param: EnderecoParam = Depends(),
    session: AsyncSession = Depends(get_session)
):
    try:
        service = EnderecoService(session=session)
        result = await service.delete(id=param.id_endereco)

        if not result:
            raise HTTPException(status_code=404, detail="Endereço não encontrado")
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)
