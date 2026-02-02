import strawberry
from strawberry.types import Info

from app.application.mappers.neutral_mapper import to_neutral_dict
from app.application.validators.schema_validator import validate_schema
from app.core.exception import raise_graphql_error
from app.domain.services.danfe_service import DanfeService
from app.infraestructure.database.repositories.danfe_repository_impl import DanfeRepositoryImpl
from app.presentation.graphql.inputs.danfe_input import DanfeFilterInput, DanfeFilterLastSevenDaysInput, DanfeFilterMonthlyInput, DanfeOrderInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.schemas.danfe_schema import DanfeInputSchema, DanfeLastSevenDaysInputSchema, DanfeMonthlyInputSchema, DanfeOrderSchema
from app.presentation.graphql.types.danfe_type import PaginatedResponseDanfeLastSevenDaysType, PaginatedResponseDanfeMonthlyType, PaginatedResponseDanfeListType
from app.presentation.graphql.types.pagination_type import PaginationType


@strawberry.type
class DanfeQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        offset: int | None = None,
        limit: int | None = None,
        filter: DanfeFilterInput | None = None,
        order: DanfeOrderInput | None = None
    ) -> PaginatedResponseDanfeListType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_schema(
                data=filter,
                schema=DanfeInputSchema
            )

            neutral_order = to_neutral_dict(obj=order)
            validate_schema(
                data=neutral_order,
                schema=DanfeOrderSchema
            )

            pagination = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            repo = DanfeRepositoryImpl(session=session)
            service = DanfeService(repo=repo)

            total, items = await service.get_list(
                pagination=pagination,
                filter=neutral_filter,
                order=neutral_order
            )

            total, items = await service.get_list(
                pagination=pagination,
                filter=neutral_filter,
                order=neutral_order
            )

            result = PaginatedResponseDanfeListType(
                pagination=PaginationType(
                    offset=pagination.offset,
                    limit=pagination.limit,
                    total=total,
                    accept_ranges=pagination.max_limit
                ),
                items=items
            )

            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_last_seven_days(
        self,
        *,
        info: Info,
        offset: int | None = None,
        limit: int | None = None,
        filter: DanfeFilterLastSevenDaysInput
    ) -> PaginatedResponseDanfeLastSevenDaysType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_schema(
                data=filter,
                schema=DanfeLastSevenDaysInputSchema
            )

            pagination = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            repo = DanfeRepositoryImpl(session=session)
            service = DanfeService(repo=repo)

            total, items = await service.get_last_seven_days(
                pagination=pagination,
                filter=neutral_filter
            )

            result = PaginatedResponseDanfeLastSevenDaysType(
                pagination=PaginationType(
                    offset=pagination.offset,
                    limit=pagination.limit,
                    total=total,
                    accept_ranges=pagination.max_limit,
                ),
                items=items
            )

            return result
        except Exception as e:
            raise_graphql_error(exc=e)


    @strawberry.field
    async def get_monthly(
        self,
        *,
        info: Info,
        offset: int | None = None,
        limit: int | None = None,
        filter: DanfeFilterMonthlyInput
    ) -> PaginatedResponseDanfeMonthlyType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_schema(
                data=filter,
                schema=DanfeMonthlyInputSchema
            )

            pagination = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            repo = DanfeRepositoryImpl(session=session)
            service = DanfeService(repo=repo)

            total, items = await service.get_monthly(
                pagination=pagination,
                filter=neutral_filter
            )

            result = PaginatedResponseDanfeMonthlyType(
                pagination=PaginationType(
                    offset=pagination.offset,
                    limit=pagination.limit,
                    total=total,
                    accept_ranges=pagination.max_limit,
                ),
                items=items
            )

            return result
        except Exception as e:
            raise_graphql_error(exc=e)
