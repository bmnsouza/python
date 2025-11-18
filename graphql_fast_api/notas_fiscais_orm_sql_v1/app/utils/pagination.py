from typing import Any, List, Dict
from app.core.constants import DEFAULT_PAGE_SIZE


def calculate_offset(page: int) -> int:
    return (page - 1) * DEFAULT_PAGE_SIZE


def format_result(data: List[Any], page: int = 1, page_size: int = DEFAULT_PAGE_SIZE) -> Dict[str, Any]:
    """
    Monta o objeto de paginação com um formato padronizado.
    """
    result = {
        "page": page,
        "page_size": page_size,
        "data": data,
    }

    return result
