from typing import List, Protocol

from app.presentation.graphql.mappers.pagination_mapper import Pagination


class ContribuinteRepository(Protocol):

    async def count_list(
        self,
        filter: dict | None = None
    ) -> int:
        ...


    async def get_list(
        self,
        *,
        pagination: Pagination,
        filter: dict | None = None,
        order: dict | None = None
    ) -> List[dict]:
        ...
