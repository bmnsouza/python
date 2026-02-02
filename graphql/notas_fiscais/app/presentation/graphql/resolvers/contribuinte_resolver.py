import strawberry
from strawberry.types import Info

from app.application.mappers.neutral_mapper import to_neutral_dict
from app.application.validators.schema_validator import validate_schema
from app.core.exception import raise_graphql_error
from app.domain.services.contribuinte_service import ContribuinteService
from app.infraestructure.database.repositories.contribuinte_repository_impl import ContribuinteRepositoryImpl
from app.presentation.graphql.inputs.contribuinte_input import ContribuinteOrderInput, ContribuinteFilterInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.schemas.contribuinte_schema import ContribuinteInputSchema, ContribuinteOrderSchema
from app.presentation.graphql.types.contribuinte_type import PaginatedResponseContribuinteListType
from app.presentation.graphql.types.pagination_type import PaginationType


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        offset: int | None = None,
        limit: int | None = None,
        filter: ContribuinteFilterInput | None = None,
        order: ContribuinteOrderInput | None = None
    ) -> PaginatedResponseContribuinteListType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_schema(
                data=neutral_filter,
                schema=ContribuinteInputSchema
            )

            neutral_order = to_neutral_dict(obj=order)
            validate_schema(
                data=neutral_order, 
                schema=ContribuinteOrderSchema
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
