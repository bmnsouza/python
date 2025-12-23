from typing import Optional
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
    filters = params.model_dump(exclude_none=True)

    # Detecta parâmetros inválidos na URL
    reserved = {"asc", "des", "offset", "limit", "fields"}
    allowed = set(filters.keys()) | reserved

    for key in request.query_params:
        if key not in allowed:
            raise HTTPException(
                status_code=400,
                detail=f"Filtro inválido: {key}"
            )

    return filters


def set_order_params(request: Request, model: DeclarativeMeta):
    seen = {}

    # Campos diretos da tabela
    table_fields = set(model.__table__.columns.keys())

    # Relacionamentos
    relationships = model.__mapper__.relationships

    # Mapa completo de campos válidos
    valid_fields = set(table_fields)

    for rel_name, rel in relationships.items():
        target_model = rel.mapper.class_
        target_columns = target_model.__table__.columns.keys()

        # permite ordenar por relacionamento direto (FK / join)
        valid_fields.add(rel_name)

        # permite relacionamento.campo
        for col in target_columns:
            valid_fields.add(f"{rel_name}.{col}")

    # Processa query params
    for key, value in request.query_params.multi_items():
        if key not in ("asc", "des"):
            continue

        direction = "asc" if key == "asc" else "des"

        for field in value.split(","):
            field = field.strip()

            # Validação forte
            if field not in valid_fields:
                raise HTTPException(
                    status_code=400,
                    detail=f"Campo inválido para ordenação: '{field}'"
                )

            # Conflito asc + des
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
