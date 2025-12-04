from typing import Any, Dict, List, Optional, Tuple
from fastapi import Response

DEFAULT_ACCEPT_RANGES = 50  # caso cliente não informe


def parse_fields_param(fields: Optional[str]) -> Optional[List[str]]:
    if not fields:
        return None
    return [f.strip() for f in fields.split(",") if f.strip()]


# def select_fields_from_obj(obj: Dict[str, Any], fields: Optional[List[str]]) -> Dict[str, Any]:
#     """Retorna apenas os campos solicitados (se fields for None, retorna tudo)."""
#     if not fields:
#         return obj
#     return {k: v for k, v in obj.items() if k in fields}


def select_fields_from_obj(obj, fields: Optional[List[str]] = None):
    if isinstance(obj, dict):
        obj_dict = obj
    else:  # Pydantic model ou SQLAlchemy model
        obj_dict = obj.dict()  # Pydantic
        # Para SQLAlchemy: obj_dict = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}

    if not fields:
        return obj_dict
    return {k: v for k, v in obj_dict.items() if k in fields}


def build_order_by_clause(asc: Optional[str], des: Optional[str]) -> List[Tuple[str, str]]:
    """
    Retorna lista de tuplas (campo, direcao) onde direcao é 'asc' ou 'desc'.
    Prioridade: asc (aplicada em ordem) depois des.
    """
    order: List[Tuple[str, str]] = []
    if asc:
        order += [(f.strip(), "asc") for f in asc.split(",") if f.strip()]
    if des:
        order += [(f.strip(), "desc") for f in des.split(",") if f.strip()]
    return order


def set_pagination_headers(response: Response, offset: int, limit: int, total: int, accept_ranges: Optional[int]):
    """
    Define headers Content-Range e Accept-Ranges e ajusta status code:
    - se offset+limit < total -> 206 Partial Content
    - else 200
    """
    if accept_ranges is None:
        accept_ranges = DEFAULT_ACCEPT_RANGES

    # Content-Range minimal: total (mantive compatibilidade com sua spec)
    response.headers["Content-Range"] = str(total)
    response.headers["Accept-Ranges"] = str(accept_ranges)

    # detalhe opcional mais informativo
    start = offset
    end = min(offset + limit - 1, total - 1) if total > 0 else 0
    response.headers["Content-Range-Detail"] = f"items {start}-{end}/{total}"

    # status
    if offset + limit < total:
        response.status_code = 206
    else:
        response.status_code = 200
