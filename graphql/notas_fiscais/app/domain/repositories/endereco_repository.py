from typing import List, Protocol

from app.presentation.graphql.mappers.pagination_mapper import Pagination


class EnderecoRepository(Protocol):

    async def count_list(
        self,
        filter: dict | None
    ) -> int:
        ...


    async def get_list(
        self,
        *,
        pagination: Pagination,
        filter: dict | None,
        order: dict | None
    ) -> List[dict]:
        ...
