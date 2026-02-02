from typing import Optional, NamedTuple

from app.core.constants import ACCEPT_RANGES
from app.core.exception import raise_graphql_error


class Pagination(NamedTuple):
    offset: int
    limit: int
    max_limit: int


def _validate_pagination(
    *,
    offset: Optional[int],
    limit: Optional[int],
) -> None:
    if offset is not None and offset < 0:
        raise_graphql_error(description="offset deve ser >= 0")

    if limit is not None and limit < 1:
        raise_graphql_error(description="limit deve ser >= 1")


def _normalize_pagination(
    *,
    offset: Optional[int],
    limit: Optional[int],
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
    offset: Optional[int],
    limit: Optional[int],
) -> Pagination:
    """
    Mapper de paginação:
    - Valida dados vindos do adapter (GraphQL / HTTP)
    - Normaliza valores
    - Retorna estrutura neutra para o use case
    """
    _validate_pagination(offset=offset, limit=limit)
    return _normalize_pagination(offset=offset, limit=limit)
