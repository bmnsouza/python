from typing import Any, Optional, Type

from graphql import GraphQLError
from pydantic import BaseModel

from app.core.exception.graphql_exception import raise_graphql_error
from app.core.response.core_response import ResponseValidationError, get_schema_fields, normalize_pagination, validate_and_build_order
from app.graphql.input.graphql_input import OrderInput


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
