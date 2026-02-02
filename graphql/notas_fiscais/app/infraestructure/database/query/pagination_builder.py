from typing import Dict, Tuple

from app.presentation.graphql.mappers.pagination_mapper import Pagination


def build_pagination(pagination: Pagination) -> Tuple[str, Dict[str, int]]:
    if pagination is None:
        raise TypeError("pagination não pode ser None")

    sql = """
    OFFSET :offset ROWS
    FETCH NEXT :limit ROWS ONLY
    """

    params = {
        "offset": pagination.offset,
        "limit": pagination.limit,
    }

    return sql, params
