from typing import List, Protocol

from app.presentation.graphql.mappers.pagination_mapper import Pagination


class DanfeRepository(Protocol):

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


    async def count_last_seven_days(
        self,
        filter: dict
    ) -> int:
        ...


    async def get_last_seven_days(
        self,
        *,
        pagination: Pagination,
        filter: dict
    ) -> List[dict]:
        ...


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
