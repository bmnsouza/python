from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_session
from app.fastapi.schema.endereco_schema import Endereco, EnderecoCreate, EnderecoUpdate
from app.fastapi.utils.exception_util import raise_http_exception
from app.fastapi.utils.field_util import validate_fields_param, select_fields_from_obj
from app.fastapi.utils.response_util import set_filters_params, set_order_params, set_pagination_params, set_pagination_headers
from app.fastapi.validator.endereco_validator import EnderecoParams, EnderecoPath
from app.model.endereco_model import EnderecoModel
from app.service.endereco_service import EnderecoService


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
        # Monta filtros, ordenação e normaliza parâmetros
        filters = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, model=EnderecoModel)
        order = set_order_params(request=request, model=EnderecoModel)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        # Chama o service passando os valores normalizados
        service = EnderecoService(session=session)
        total, items = await service.get_list(offset=final_offset, limit=final_limit, filters=filters, order=order)

        # Aplica headers
        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        # Transformação de campos
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
        # Monta filtros, ordenação e normaliza parâmetros
        filters = set_filters_params(request=request, params=params)
        requested_fields = validate_fields_param(fields=fields, model=EnderecoModel)
        order = set_order_params(request=request, model=EnderecoModel)
        final_offset, final_limit, final_accept_ranges = set_pagination_params(offset=offset, limit=limit)

        # Chama o service passando os valores normalizados
        service = EnderecoService(session=session)
        total, items = await service.get_list_sql(offset=final_offset, limit=final_limit, filters=filters, order=order)

        # Aplica headers
        set_pagination_headers(response=response, offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges)

        # Transformação de campos
        transformed = [select_fields_from_obj(i, requested_fields) for i in items]

        return transformed
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.get("/{id_endereco}", response_model=Endereco)
async def get_by_id(path: EnderecoPath = Depends(), session: AsyncSession = Depends(get_session)):
    try:
        service = EnderecoService(session=session)
        result = await service.get_by_id(id=path.id_endereco)
    except HTTPException:
        raise
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
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)


@router.put("/{id_endereco}", response_model=Endereco)
async def update(path: EnderecoPath = Depends(), endereco: EnderecoUpdate = ..., session: AsyncSession = Depends(get_session)):
    try:
        service = EnderecoService(session=session)
        result = await service.update(id=path.id_endereco, data=endereco.model_dump(exclude_unset=True))
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    return result


@router.delete("/{id_endereco}", status_code=204)
async def delete(path: EnderecoPath = Depends(), session: AsyncSession = Depends(get_session)):
    try:
        service = EnderecoService(session=session)
        result = await service.delete(id=path.id_endereco)
    except HTTPException:
        raise
    except Exception as e:
        raise_http_exception(exc=e)

    if not result:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
