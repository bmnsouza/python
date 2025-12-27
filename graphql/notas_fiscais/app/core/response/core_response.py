from typing import Any, Iterable, Optional, Set, Type

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeMeta

from app.core.constants import ACCEPT_RANGES


class ResponseValidationError(Exception):
    """Erro de validação independente de transporte."""


def get_orm_fields(model: DeclarativeMeta) -> Set[str]:
    fields = set(model.__table__.columns.keys())

    for rel_name, rel in model.__mapper__.relationships.items():
        fields.add(rel_name)
        for col in rel.mapper.class_.__table__.columns.keys():
            fields.add(f"{rel_name}.{col}")

    return fields


def get_schema_fields(schema: Type) -> Set[str]:
    if hasattr(schema, "model_fields"):
        return set(schema.model_fields.keys())

    if hasattr(schema, "__annotations__"):
        return set(schema.__annotations__.keys())

    return set()


def validate_and_build_order(
    items: Iterable[tuple[str, str]],
    valid_fields: Set[str],
) -> list[tuple[str, str]]:
    seen: dict[str, str] = {}

    for direction, raw in items:
        for field in raw.split(","):
            field = field.strip()

            if field not in valid_fields:
                raise ResponseValidationError(
                    f"Campo inválido para ordenação: '{field}'"
                )

            if field in seen and seen[field] != direction:
                raise ResponseValidationError(
                    f"Campo '{field}' não pode ser asc e des ao mesmo tempo"
                )

            seen[field] = direction

    return list(seen.items())


def normalize_filters(params: Any) -> dict | None:
    if params is None:
        return None

    if isinstance(params, BaseModel):
        return params.model_dump(exclude_none=True)

    if isinstance(params, dict):
        return {k: v for k, v in params.items() if v is not None}

    if hasattr(params, "__dict__"):
        return {k: v for k, v in vars(params).items() if v is not None}

    raise TypeError(f"Tipo inválido para filtros: {type(params)}")


def validate_query_params(received: set[str], allowed: set[str]) -> None:
    invalid = received - allowed
    if invalid:
        raise ResponseValidationError(
            f"Parâmetro(s) inválido(s): {', '.join(sorted(invalid))}"
        )


def normalize_pagination(
    offset: Optional[int],
    limit: Optional[int],
) -> tuple[int, int, int]:
    accept_ranges = ACCEPT_RANGES
    offset = offset if offset is not None else 0
    limit = limit if limit is not None else accept_ranges
    limit = min(limit, accept_ranges)

    return offset, limit, accept_ranges
