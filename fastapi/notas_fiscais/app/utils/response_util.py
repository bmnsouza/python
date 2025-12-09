from typing import List, Optional, Tuple
from fastapi import Query, Request, Response


# Regras do servidor
ACCEPT_RANGES = 200

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


def set_filters_order(request: Request, asc: Optional[str] = Query(None), des: Optional[str] = Query(None)):
    raw_params = dict(request.query_params)
    reserved = {"asc", "des", "offset", "limit", "fields", "accept_ranges"}
    filters = {k: v for k, v in raw_params.items() if k not in reserved}
    order = build_order_by_clause(asc, des)

    return filters, order


def build_order_by_clause(asc: Optional[str], des: Optional[str]) -> List[Tuple[str, str]]:
    """
    Retorna lista de tuplas (campo, direcao) onde direcao é 'asc' ou 'desc'.
    Prioridade: asc (aplicada em ordem) depois desc.
    """
    order: List[Tuple[str, str]] = []
    if asc:
        order += [(f.strip(), "asc") for f in asc.split(",") if f.strip()]
    if des:
        order += [(f.strip(), "desc") for f in des.split(",") if f.strip()]
    return order


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
