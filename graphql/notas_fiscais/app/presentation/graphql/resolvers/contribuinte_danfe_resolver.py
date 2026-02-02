import strawberry
from strawberry.types import Info

from app.application.mappers.neutral_mapper import to_neutral_dict
from app.application.validators.input_validator import validate_input
from app.core.exception import raise_graphql_error
from app.domain.services.contribuinte_danfe_service import ContribuinteDanfeService
from app.infraestructure.database.repositories.contribuinte_danfe_repository_impl import ContribuinteDanfeRepositoryImpl
from app.presentation.graphql.inputs.contribuinte_danfe_input import ContribuinteDanfeMonthlyFilterInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.types.contribuinte_danfe_type import PaginatedResponseContribuinteDanfeMonthlyType
from app.presentation.graphql.types.pagination_type import PaginationType
from app.presentation.graphql.validators.contribuinte_danfe_validator import ContribuinteDanfeMonthlyFilterInputValidator


@strawberry.type
class ContribuinteDanfeQuery:

    @strawberry.field
    async def get_monthly(
        self,
        info: Info,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter: ContribuinteDanfeMonthlyFilterInput
    ) -> PaginatedResponseContribuinteDanfeMonthlyType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_input(
                data=filter,
                schema=ContribuinteDanfeMonthlyFilterInputValidator
            )

            pagination = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            repo = ContribuinteDanfeRepositoryImpl(session=session)
            service = ContribuinteDanfeService(repo=repo)

            total, items = await service.get_monthly(
                pagination=pagination,
                filter=neutral_filter
            )

            result = PaginatedResponseContribuinteDanfeMonthlyType(
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
