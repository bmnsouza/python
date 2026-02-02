import strawberry
from strawberry.types import Info

from app.application.mappers.neutral_mapper import to_neutral_dict
from app.application.validators.input_validator import validate_input
from app.core.exception import raise_graphql_error
from app.domain.services.endereco_service import EnderecoService
from app.infraestructure.database.repositories.endereco_repository_impl import EnderecoRepositoryImpl
from app.presentation.graphql.inputs.endereco_input import EnderecoListFilterInput, EnderecoListOrderInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.presentation.graphql.types.endereco_type import PaginatedResponseEnderecoListType
from app.presentation.graphql.types.pagination_type import PaginationType
from app.presentation.graphql.validators.endereco_validator import EnderecoListFilterInputValidator, EnderecoListOrderInputValidator


@strawberry.type
class EnderecoQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        *,
        offset: int | None = None,
        limit: int | None = None,
        filter: EnderecoListFilterInput | None = None,
        order: EnderecoListOrderInput | None = None
    ) -> PaginatedResponseEnderecoListType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_input(
                data=neutral_filter,
                schema=EnderecoListFilterInputValidator
            )

            neutral_order = to_neutral_dict(obj=order)
            validate_input(
                data=neutral_order,
                schema=EnderecoListOrderInputValidator
            )

            pagination = map_pagination(offset=offset, limit=limit)

            session = info.context["session"]
            repo = EnderecoRepositoryImpl(session=session)
            service = EnderecoService(repo=repo)

            total, items = await service.get_list(
                pagination=pagination,
                filter=neutral_filter,
                order=neutral_order
            )

            result = PaginatedResponseEnderecoListType(
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
