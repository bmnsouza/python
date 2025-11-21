from typing import Any, Dict, Optional


# Constantes
DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 100


def calculate_offset(page: int) -> int:
    return (page - 1) * DEFAULT_PAGE_SIZE


def format_result(data: Any, page: Optional[int] = None) -> Dict[str, Any]:
    # Sem paginação
    if page is None:
        return {
            "data": data
        }

    # Com paginação
    return {
        "page": page,
        "page_size": DEFAULT_PAGE_SIZE,
        "data": data
    }
