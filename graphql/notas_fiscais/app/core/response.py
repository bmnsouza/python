from typing import Any, Iterable, Optional, Set, Type

from graphql import GraphQLError
from pydantic import BaseModel

from app.core.constants import ACCEPT_RANGES
from app.core.exception import raise_graphql_error
from app.presentation.graphql.inputs.order_input import OrderInput


class ResponseValidationError(Exception):
    """Erro de validação independente de transporte."""


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


def normalize_pagination(
    offset: Optional[int],
    limit: Optional[int],
) -> tuple[int, int, int]:
    accept_ranges = ACCEPT_RANGES
    offset = offset if offset is not None else 0
    limit = limit if limit is not None else accept_ranges
    limit = min(limit, accept_ranges)

    return offset, limit, accept_ranges


def validate_params(
    *,
    params: Any,
    schema: Type[BaseModel]
) -> dict:
    if params is None:
        return {}

    # Converte Input GraphQL / objeto em dict
    if isinstance(params, BaseModel):
        data = params.model_dump(exclude_none=True)

    elif hasattr(params, "__dict__"):
        data = {
            k: v
            for k, v in vars(params).items()
            if v is not None
        }

    elif isinstance(params, dict):
        data = {
            k: v
            for k, v in params.items()
            if v is not None
        }

    else:
        raise TypeError(f"Tipo inválido para validação: {type(params)}")

    # Validação (lança exceção se inválido)
    validated = schema(**data)

    # Retorno normalizado
    return validated.model_dump(exclude_none=True)


def set_order_params(
    order: list[OrderInput],
    schema: Type[BaseModel]
) -> list[tuple[str, str]]:
    if not order:
        return []

    if not schema:
        raise GraphQLError("Informe o schema para validação da ordenação")

    valid_fields = set()

    if schema:
        valid_fields |= get_schema_fields(schema)

    items = [(o.direction.value.lower(), o.field) for o in order]

    try:
        return validate_and_build_order(items, valid_fields)
    except ResponseValidationError as exc:
        raise GraphQLError(str(exc))


def set_pagination_params(
    offset: Optional[int],
    limit: Optional[int],
) -> tuple[int, int, int]:
    if offset is not None and offset < 0:
        raise_graphql_error(description="offset deve ser >= 0")

    if limit is not None and limit < 1:
        raise_graphql_error(description="limit deve ser >= 1")

    return normalize_pagination(offset, limit)
