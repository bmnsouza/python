from typing import List, Protocol

from app.presentation.graphql.mappers.pagination_mapper import Pagination


class DanfeRepository(Protocol):

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


    async def count_last_seven_days(
        self,
        filter: dict | None
    ) -> int:
        ...


    async def get_last_seven_days(
        self,
        *,
        pagination: Pagination,
        filter: dict | None
    ) -> List[dict]:
        ...


    async def count_monthly(
        self,
        filter: dict | None
    ) -> int:
        ...


    async def get_monthly(
        self,
        *,
        pagination: Pagination,
        filter: dict | None
    ) -> List[dict]:
        ...
