from typing import Optional, Type

from graphql import GraphQLError
from pydantic import BaseModel

from app.graphql.schema.input.graphql_input import OrderInput
from app.core.exception.exception_graphql import raise_graphql_error
from app.core.response.response_core import (
    ResponseValidationError,
    get_schema_fields,
    normalize_filters,
    normalize_pagination,
    validate_and_build_order
)


def validate_params(*, params, schema: Type[BaseModel]) -> None:
    if params is None:
        return

    if hasattr(params, "__dict__"):
        data = params.__dict__
    elif isinstance(params, dict):
        data = params
    else:
        raise TypeError(f"Tipo inválido para validação: {type(params)}")

    schema(**data)


def set_filters_params(params):
    return normalize_filters(params)


def set_order_params(
    order: list[OrderInput] | None,
    schema: Type[BaseModel] | None = None,
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
