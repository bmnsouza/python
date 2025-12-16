from typing import Optional
from fastapi import Request, Response
from sqlalchemy.orm import DeclarativeMeta


# Regras do servidor
ACCEPT_RANGES = 200


def set_filters_params(request: Request):
    raw_params = dict(request.query_params)
    reserved = {"asc", "des", "offset", "limit", "fields"}
    filters = {k: v for k, v in raw_params.items() if k not in reserved}
    return filters


def set_order_params(request: Request, model: DeclarativeMeta):
    """
    Processa asc/des na ordem exata enviada, expande imediatamente cada parâmetro, ignora campos inexistentes e mantém apenas a primeira ocorrência de cada campo.
    """
    order_raw = []
    seen = set()

    # Mantém a ordem exata da URL
    for key, value in request.query_params.multi_items():
        if key in ("asc", "des"):
            direction = "asc" if key == "asc" else "des"
            fields = [f.strip() for f in value.split(",") if f.strip()]

            for field in fields:
                if hasattr(model, field):
                    order_raw.append((field, direction))

    # Remove duplicados preservando a primeira ocorrência
    order_final = []
    for field, direction in order_raw:
        if field not in seen:
            seen.add(field)
            order_final.append((field, direction))

    return order_final


def normalize_pagination_params(offset: Optional[int], limit: Optional[int]) -> tuple[int, int, int]:
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
