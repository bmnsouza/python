import strawberry
from strawberry.types import Info

from app.core.exception import raise_graphql_error
from app.domain.services.danfe_service import DanfeService
from app.presentation.graphql.inputs.danfe_input import DanfeFilterInput, DanfeFilterLastSevenDaysInput, DanfeFilterMonthlyInput, DanfeOrderInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.mappers.schema_mapper import map_to_schema
from app.presentation.graphql.schemas.danfe_schema import DanfeLastSevenDaysSchema, DanfeMonthlySchema, DanfeSchema
from app.presentation.graphql.types.danfe_type import PaginatedResponseDanfeLastSevenDaysType, PaginatedResponseDanfeMonthlyType, PaginatedResponseDanfeType
from app.presentation.graphql.types.pagination_type import PaginationType


@strawberry.type
class DanfeQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        filter: DanfeFilterInput | None = None,
        order: DanfeOrderInput | None = None,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeType:
        try:
            filter_schema = map_to_schema(data=filter, schema=DanfeSchema)
            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_list(offset=final_offset, limit=final_limit, filter=filter_schema, order=order)

            result = PaginatedResponseDanfeType(pagination=PaginationType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges), items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_last_seven_days(
        self,
        info: Info,
        filter: DanfeFilterLastSevenDaysInput,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeLastSevenDaysType:
        try:
            filter_schema = map_to_schema(data=filter, schema=DanfeLastSevenDaysSchema)
            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_last_seven_days(offset=final_offset, limit=final_limit, filter=filter_schema)

            result = PaginatedResponseDanfeLastSevenDaysType(pagination=PaginationType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges), items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_monthly(
        self,
        info: Info,
        filter: DanfeFilterMonthlyInput,
        offset: int | None = None,
        limit: int | None = None
    ) -> PaginatedResponseDanfeMonthlyType:
        try:
            filter_schema = map_to_schema(data=filter, schema=DanfeMonthlySchema)
            final_offset, final_limit, final_accept_ranges = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            service = DanfeService(session=session)
            total, items = await service.get_monthly(offset=final_offset, limit=final_limit, filter=filter_schema)

            result = PaginatedResponseDanfeMonthlyType(pagination=PaginationType(offset=final_offset, limit=final_limit, total=total, accept_ranges=final_accept_ranges), items=items)
            return result
        except Exception as e:
            raise_graphql_error(exc=e)
