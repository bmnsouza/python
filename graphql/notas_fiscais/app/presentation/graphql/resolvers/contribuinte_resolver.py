import strawberry
from strawberry.types import Info

from app.application.mappers.neutral_mapper import to_neutral_dict
from app.application.validators.input_validator import validate_input
from app.core.exception import raise_graphql_error
from app.domain.services.contribuinte_service import ContribuinteService
from app.infraestructure.database.repositories.contribuinte_repository_impl import ContribuinteRepositoryImpl
from app.presentation.graphql.inputs.contribuinte_input import ContribuinteListOrderInput, ContribuinteListFilterInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.types.contribuinte_type import PaginatedResponseContribuinteListType
from app.presentation.graphql.types.pagination_type import PaginationType
from app.presentation.graphql.validators.contribuinte_validator import ContribuinteListFilterInputValidator, ContribuinteListOrderInputValidator


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter: ContribuinteListFilterInput | None = None,
        order: ContribuinteListOrderInput | None = None
    ) -> PaginatedResponseContribuinteListType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_input(
                data=neutral_filter,
                schema=ContribuinteListFilterInputValidator
            )

            neutral_order = to_neutral_dict(obj=order)
            validate_input(
                data=neutral_order,
                schema=ContribuinteListOrderInputValidator
            )

            pagination = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            repo = ContribuinteRepositoryImpl(session=session)
            service = ContribuinteService(repo=repo)

            total, items = await service.get_list(
                pagination=pagination,
                filter=neutral_filter,
                order=neutral_order
            )

            result = PaginatedResponseContribuinteListType(
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
