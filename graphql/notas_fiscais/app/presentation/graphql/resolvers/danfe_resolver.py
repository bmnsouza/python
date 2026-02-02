import strawberry
from strawberry.types import Info

from app.application.mappers.neutral_mapper import to_neutral_dict
from app.application.validators.input_validator import validate_input
from app.core.exception import raise_graphql_error
from app.domain.services.danfe_service import DanfeService
from app.infraestructure.database.repositories.danfe_repository_impl import DanfeRepositoryImpl
from app.presentation.graphql.inputs.danfe_input import DanfeListFilterInput, DanfeLastSevenDaysFilterInput, DanfeMonthlyFilterInput, DanfeListOrderInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.types.danfe_type import PaginatedResponseDanfeLastSevenDaysType, PaginatedResponseDanfeMonthlyType, PaginatedResponseDanfeListType
from app.presentation.graphql.types.pagination_type import PaginationType
from app.presentation.graphql.validators.danfe_validator import DanfeLastSevenDaysFilterInputValidator, DanfeListFilterInputValidator, DanfeListOrderInputValidator, DanfeMonthlyFilterInputValidator


@strawberry.type
class DanfeQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter: DanfeListFilterInput | None = None,
        order: DanfeListOrderInput | None = None
    ) -> PaginatedResponseDanfeListType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_input(
                data=filter,
                schema=DanfeListFilterInputValidator
            )

            neutral_order = to_neutral_dict(obj=order)
            validate_input(
                data=neutral_order,
                schema=DanfeListOrderInputValidator
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
        info: Info,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter: DanfeLastSevenDaysFilterInput
    ) -> PaginatedResponseDanfeLastSevenDaysType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_input(
                data=filter,
                schema=DanfeLastSevenDaysFilterInputValidator
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
        info: Info,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter: DanfeMonthlyFilterInput
    ) -> PaginatedResponseDanfeMonthlyType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_input(
                data=filter,
                schema=DanfeMonthlyFilterInputValidator
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
