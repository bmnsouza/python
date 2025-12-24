from typing import Optional, Type
from fastapi import HTTPException, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeMeta

from app.core.constants import ACCEPT_RANGES


def set_filters_params(request: Request, params: BaseModel) -> dict:
    """
    Combina:
    - Query params validados via Pydantic
    - Rejeita parâmetros não permitidos na URL
    """
    params = params.model_dump(exclude_none=True)

    # Detecta parâmetros inválidos na URL
    reserved = {"asc", "des", "offset", "limit", "fields"}
    allowed = set(params.keys()) | reserved

    for key in request.query_params:
        if key not in allowed:
            raise HTTPException(
                status_code=400,
                detail=f"Parâmetro inválido: {key}"
            )

    return params


def set_order_params(
    request: Request,
    *,
    orm_model: Optional[DeclarativeMeta] = None,
    schema: Optional[Type[BaseModel]] = None,
):
    if not orm_model and not schema:
        raise ValueError("Informe orm_model ou schema")

    seen = {}

    valid_fields = set()

    # ORM
    if orm_model:
        table_fields = set(orm_model.__table__.columns.keys())
        valid_fields |= table_fields

        for rel_name, rel in orm_model.__mapper__.relationships.items():
            target_model = rel.mapper.class_
            target_columns = target_model.__table__.columns.keys()

            valid_fields.add(rel_name)
            for col in target_columns:
                valid_fields.add(f"{rel_name}.{col}")

    # Schema (SQL nativo)
    if schema:
        valid_fields |= set(schema.model_fields.keys())

    # Processa query params
    for key, value in request.query_params.multi_items():
        if key not in ("asc", "des"):
            continue

        direction = "asc" if key == "asc" else "des"

        for field in value.split(","):
            field = field.strip()

            if field not in valid_fields:
                raise HTTPException(
                    status_code=400,
                    detail=f"Campo inválido para ordenação: '{field}'"
                )

            if field in seen and seen[field] != direction:
                raise HTTPException(
                    status_code=400,
                    detail=f"Campo '{field}' não pode ser asc e des ao mesmo tempo"
                )

            seen[field] = direction

    return list(seen.items())


def set_pagination_params(offset: Optional[int], limit: Optional[int]) -> tuple[int, int, int]:
    """
    Retorna (offset_normalized, limit_normalized, accept_ranges_effective)
    Regras:
    - accept_ranges default = server_max
    - offset default = 0
    - limit default = accept_ranges
    - limit não pode ultrapassar accept_ranges
    """
    accept_ranges = ACCEPT_RANGES
    offset = offset if offset is not None else 0
    limit = limit if limit is not None else accept_ranges
    limit = min(limit, accept_ranges)

    return offset, limit, accept_ranges


def set_pagination_headers(response: Response, offset: int, limit: int, total: int, accept_ranges: int) -> None:
    """
    Recebe valores já normalizados (offset, limit, accept_ranges).
    Define Content-Range, Accept-Ranges e response.status_code.
    """
    start = offset
    end = min(offset + limit - 1, total - 1) if total > 0 else 0

    response.headers["Accept-Ranges"] = str(accept_ranges)
    response.headers["Content-Range"] = f"items {start}-{end}/{total}"

    if end + 1 < total:
        response.status_code = 206  # Partial Content
    else:
        response.status_code = 200  # OK
