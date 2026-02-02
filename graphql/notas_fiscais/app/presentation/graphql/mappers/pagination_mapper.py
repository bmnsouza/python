from typing import NamedTuple

from app.core.constants import ACCEPT_RANGES
from app.core.exception import raise_graphql_error


class Pagination(NamedTuple):
    offset: int
    limit: int
    max_limit: int


def _validate_pagination(
    *,
    offset:  int | None,
    limit:  int | None
) -> None:
    if offset is not None and offset < 0:
        raise_graphql_error(description="offset deve ser >= 0")

    if limit is not None and limit < 1:
        raise_graphql_error(description="limit deve ser >= 1")


def _normalize_pagination(
    *,
    offset:  int | None,
    limit:  int | None
) -> Pagination:
    max_limit = ACCEPT_RANGES

    normalized_offset = offset or 0
    normalized_limit = limit or max_limit
    normalized_limit = min(normalized_limit, max_limit)

    return Pagination(
        offset=normalized_offset,
        limit=normalized_limit,
        max_limit=max_limit,
    )


def map_pagination(
    *,
    offset:  int | None,
    limit:  int | None
) -> Pagination:
    _validate_pagination(offset=offset, limit=limit)
    return _normalize_pagination(offset=offset, limit=limit)
