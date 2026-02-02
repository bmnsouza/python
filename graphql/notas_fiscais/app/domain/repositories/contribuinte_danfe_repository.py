from typing import List, Protocol

from app.presentation.graphql.mappers.pagination_mapper import Pagination


class ContribuinteDanfeRepository(Protocol):

    async def count_monthly(
        self,
        filter: dict
    ) -> int:
        ...


    async def get_monthly(
        self,
        *,
        pagination: Pagination,
        filter: dict
    ) -> List[dict]:
        ...
