from functools import wraps
from typing import TypeVar

from strawberry.relay import Connection, Edge, PageInfo

from app.core.exceptions import ValidationException

from ..utils.cursor_util import Cursor

T = TypeVar("T")

MAX_PAGE_SIZE = 5


def relay_connection(resolver) -> Connection[T]:
    @wraps(resolver)
    async def wrapper(*args, **kwargs):
        # Normalização do first
        first = kwargs.get("first")
        if first is None:
            first = MAX_PAGE_SIZE
        elif first <= 0:
            raise ValidationException("'first' deve ser maior que zero")
        else:
            first = min(first, MAX_PAGE_SIZE)

        # Importante: pedimos +1 para detectar próxima página
        kwargs["first"] = first + 1

        # Decodificação do cursor
        after = kwargs.get("after")
        after_decoded = 0
        if after is not None:
            after_decoded = Cursor.decode(after)

        # Chama o resolver
        result = await resolver(*args, **kwargs)
        items = result.items

        # Detecta a próxima página
        has_next_page = len(items) > first

        # Remove o item extra e monta edges
        items = items[:first]

        edges = [
            Edge(node=item, cursor=Cursor.encode(after_decoded + i + 1))
            for i, item in enumerate(items)
        ]

        # Monta pageInfo
        page_info = PageInfo(
            has_next_page=has_next_page,
            has_previous_page=after_decoded > 0,
            start_cursor=edges[0].cursor if edges else None,
            end_cursor=edges[-1].cursor if edges else None,
        )

        # Retorna Connection
        return Connection(
            edges=edges,
            page_info=page_info,
        )

    return wrapper
