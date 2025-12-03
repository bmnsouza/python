# app/router/contribuinte_router.py
from typing import Optional, Dict, List, Tuple
from fastapi import APIRouter, Depends, Request, Response, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_session
from app.service.contribuinte_service import ContribuinteService
from app.utils.response_utils import parse_fields_param, select_fields_from_obj, build_order_by_clause, set_pagination_headers
from app.fastapi.schema.contribuinte_schema import ContribuinteCreate, ContribuinteUpdate, PaginatedOffsetResponse, SingleResponse

router = APIRouter(prefix="/v1/contribuinte", tags=["Contribuinte"])


@router.get("", response_model=List[dict])  # retornamos lista direta; headers contem meta
async def get_contribuintes(
    request: Request,
    response: Response,
    asc: Optional[str] = Query(None, description="asc=campo1,campo2"),
    des: Optional[str] = Query(None, description="des=campo1,campo2"),
    offset: int = Query(0, ge=0),
    limit: int = Query(50, ge=1),
    fields: Optional[str] = Query(None, description="fields=cd_contribuinte,nm_fantasia"),
    accept_ranges: Optional[int] = Query(None),
    session: AsyncSession = Depends(get_session)
):
    """
    Listar contribuintes com filtros simples, ordenação e paginação offset/limit.
    Qualquer query param não reservado será tratado como filtro simples (igualdade),
    exceto quando o valor contém '%' -> será usado LIKE, e quando o campo for nm_fantasia será usado ILIKE "%val%".
    """
    # captura query params brutos
    raw_params: Dict[str, str] = dict(request.query_params)

    # parâmetros reservados que não são filtros
    reserved = {"asc", "des", "offset", "limit", "fields", "accept_ranges"}

    # extrai filtros (opção A — simples)
    filters = {k: v for k, v in raw_params.items() if k not in reserved}

    order = build_order_by_clause(asc, des)

    service = ContribuinteService(session)
    total, items = await service.list_contribuintes(filters=filters, order=order, offset=offset, limit=limit)

    # seleção de campos
    requested_fields = parse_fields_param(fields)
    transformed = [select_fields_from_obj(i, requested_fields) for i in items]

    # headers
    set_pagination_headers(response, offset=offset, limit=limit, total=total, accept_ranges=accept_ranges)

    # caso nenhum resultado e offset==0 -> 404? sua versão antiga fazia 404. Aqui eu retorno [] + status apropriado.
    # Se preferir, mantenho 404 quando resultado vazio: descomente abaixo.
    # if not transformed:
    #     raise HTTPException(status_code=404, detail="Contribuinte não encontrado")

    return transformed


@router.get("/cd", response_model=SingleResponse)
async def get_contribuinte_por_cd(cd_contribuinte: str, session: AsyncSession = Depends(get_session)):
    service = ContribuinteService(session)
    result = await service.get_contribuinte_por_cd(cd_contribuinte)
    if not result:
        raise HTTPException(status_code=404, detail={"errors":[{"code":"not_found","title":"Not Found","description":"Contribuinte não encontrado"}]})
    return {"data": result}


@router.get("/cnpj", response_model=SingleResponse)
async def get_contribuinte_por_cnpj(cnpj_contribuinte: str, session: AsyncSession = Depends(get_session)):
    service = ContribuinteService(session)
    result = await service.get_contribuinte_por_cnpj(cnpj_contribuinte)
    if not result:
        raise HTTPException(status_code=404, detail={"errors":[{"code":"not_found","title":"Not Found","description":"Contribuinte não encontrado"}]})
    return {"data": result}


@router.post("/", response_model=SingleResponse, status_code=201)
async def create_contribuinte(contribuinte: ContribuinteCreate, session: AsyncSession = Depends(get_session)):
    service = ContribuinteService(session)
    result = await service.create_contribuinte(contribuinte.model_dump())
    return {"data": result}


@router.put("/{cd_contribuinte}", response_model=SingleResponse)
async def update_contribuinte(cd_contribuinte: str, contribuinte: ContribuinteUpdate, session: AsyncSession = Depends(get_session)):
    service = ContribuinteService(session)
    result = await service.update_contribuinte(cd_contribuinte, contribuinte.model_dump(exclude_unset=True))
    if not result:
        raise HTTPException(status_code=404, detail={"errors":[{"code":"not_found","title":"Not Found","description":"Contribuinte não encontrado"}]})
    return {"data": result}


@router.delete("/{cd_contribuinte}", status_code=204)
async def delete_contribuinte(cd_contribuinte: str, session: AsyncSession = Depends(get_session)):
    service = ContribuinteService(session)
    result = await service.delete_contribuinte(cd_contribuinte)
    if not result:
        raise HTTPException(status_code=404, detail={"errors":[{"code":"not_found","title":"Not Found","description":"Contribuinte não encontrado"}]})
    # 204 status => sem body
    return Response(status_code=204)
