from typing import Optional

from app.core.constants import ACCEPT_RANGES
from app.core.exception import raise_graphql_error


def normalize_pagination(
    *,
    offset: Optional[int],
    limit: Optional[int],
) -> tuple[int, int, int]:
    accept_ranges = ACCEPT_RANGES
    offset = offset if offset is not None else 0
    limit = limit if limit is not None else accept_ranges
    limit = min(limit, accept_ranges)

    return offset, limit, accept_ranges


def map_pagination(
    *,
    offset: Optional[int],
    limit: Optional[int],
) -> tuple[int, int, int]:
    if offset is not None and offset < 0:
        raise_graphql_error(description="offset deve ser >= 0")

    if limit is not None and limit < 1:
        raise_graphql_error(description="limit deve ser >= 1")

    return normalize_pagination(offset=offset, limit=limit)
