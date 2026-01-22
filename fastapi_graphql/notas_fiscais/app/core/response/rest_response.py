from collections import defaultdict
from typing import Iterable, Optional, Set, Type

from fastapi import HTTPException, Request, Response
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeMeta

from app.core.response.core_response import (
    ResponseValidationError,
    get_orm_fields,
    get_schema_fields,
    normalize_filters,
    normalize_pagination,
    validate_and_build_order,
    validate_query_params
)


def validate_fields_param(
    fields: Optional[str],
    *,
    model: Optional[DeclarativeMeta] = None,
    schema: Optional[Type[BaseModel]] = None,
) -> Optional[Set[str]]:
    if not fields:
        return None

    if not model and not schema:
        raise ValueError("Informe model ou schema")

    requested = {f.strip() for f in fields.split(",")}

    valid_fields: Set[str] = set()

    if model:
        valid_fields |= get_orm_fields(model)

    if schema:
        valid_fields |= get_schema_fields(schema)

    invalid = requested - valid_fields
    if invalid:
        raise HTTPException(
            status_code=400,
            detail=f"Campos inválidos em fields: {', '.join(sorted(invalid))}",
        )

    return requested


def select_fields_from_obj(obj, fields: Optional[Iterable[str]] = None):
    if hasattr(obj, "model_dump"):
        obj_dict = obj.model_dump()
    elif hasattr(obj, "__table__"):
        obj_dict = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
    else:
        obj_dict = obj

    if not fields:
        return obj_dict

    direct_fields = set()
    nested_fields = defaultdict(set)

    for f in fields:
        if "." in f:
            parent, child = f.split(".", 1)
            nested_fields[parent].add(child)
        else:
            direct_fields.add(f)

    result = {}

    for key, value in obj_dict.items():
        if key in direct_fields:
            result[key] = value

    for key, value in obj_dict.items():
        if key not in nested_fields:
            continue

        subfields = nested_fields[key]

        if value is None:
            continue

        if isinstance(value, list):
            result[key] = [
                {k: v for k, v in item.items() if k in subfields}
                for item in value
            ]
        elif isinstance(value, dict):
            result[key] = {k: v for k, v in value.items() if k in subfields}

    return result


def set_filters_params(
    request: Request,
    params: BaseModel,
    *,
    allow_order: bool = True,
    allow_fields: bool = True,
) -> dict:
    data = normalize_filters(params) or {}

    reserved = {"offset", "limit"}

    if allow_order:
        reserved |= {"asc", "des"}

    if allow_fields:
        reserved |= {"fields"}

    allowed = set(data.keys()) | reserved

    try:
        validate_query_params(
            received=set(request.query_params.keys()),
            allowed=allowed,
        )
    except ResponseValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    return data



def set_order_params(
    request: Request,
    schema: Type[BaseModel],
):
    if not request:
        return []

    if not schema:
        raise ValueError("Informe o schema para validação da ordenação")

    valid_fields = set()

    if schema:
        valid_fields |= get_schema_fields(schema)

    items = [
        ("asc" if key == "asc" else "des", value)
        for key, value in request.query_params.multi_items()
        if key in ("asc", "des")
    ]

    try:
        return validate_and_build_order(items, valid_fields)
    except ResponseValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


def set_pagination_params(
    offset: Optional[int],
    limit: Optional[int],
) -> tuple[int, int, int]:
    return normalize_pagination(offset, limit)


def set_pagination_headers(
    response: Response,
    offset: int,
    limit: int,
    total: int,
    accept_ranges: int,
) -> None:
    start = offset
    end = min(offset + limit - 1, total - 1) if total > 0 else 0

    response.headers["Accept-Ranges"] = str(accept_ranges)
    response.headers["Content-Range"] = f"items {start}-{end}/{total}"
    response.status_code = 206 if end + 1 < total else 200
