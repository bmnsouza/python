from typing import Dict, Tuple


def build_pagination(
    *,
    offset: int,
    limit: int,
) -> Tuple[str, Dict[str, int]]:
    sql = """
    OFFSET :offset ROWS
    FETCH NEXT :limit ROWS ONLY
    """

    params = {
        "offset": offset,
        "limit": limit,
    }

    return sql, params
