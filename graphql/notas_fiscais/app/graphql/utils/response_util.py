from typing import Any, Dict, Optional
from sqlalchemy.orm import DeclarativeMeta

from app.core.constants import ACCEPT_RANGES
from app.graphql.schema.input.contribuinte_input import ContribuinteFiltersInput
from app.graphql.schema.input.danfe_input import DanfeFiltersInput
from app.graphql.schema.input.endereco_input import EnderecoFiltersInput
from app.graphql.schema.input.graphql_input import OrderInput
from app.graphql.utils.exception_util import raise_graphql_error


def set_filters_params(filters: ContribuinteFiltersInput | DanfeFiltersInput | EnderecoFiltersInput | None) -> Dict[str, Any]:
    if not filters:
        return {}

    filters = {k: v for k, v in vars(filters).items() if v is not None}
    return filters


def set_order_params(order: list[OrderInput] | None, model: DeclarativeMeta) -> list[tuple[str, str]]:
    if not order:
        return []

    seen = set()
    result = []

    for item in order:
        field = item.field
        direction = item.direction.value

        if not hasattr(model, field):
            continue

        if field not in seen:
            seen.add(field)
            result.append((field, direction))

    return result


def set_pagination_params(offset: Optional[int], limit: Optional[int]) -> tuple[int, int, int]:
    """
    Retorna (offset_normalized, limit_normalized, accept_ranges_effective)
    Regras:
    - accept_ranges default = server_max
    - offset default = 0
    - limit default = accept_ranges
    - limit não pode ultrapassar accept_ranges
    """

    if offset is not None and offset < 0:
        raise_graphql_error(description="offset deve ser >= 0")

    if limit is not None and limit < 1:
        raise_graphql_error(description="limit deve ser >= 1")

    accept_ranges = ACCEPT_RANGES
    offset = offset if offset is not None else 0
    limit = limit if limit is not None else accept_ranges
    limit = min(limit, accept_ranges)

    return offset, limit, accept_ranges
