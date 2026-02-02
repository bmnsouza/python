import strawberry
from strawberry.types import Info

from app.application.mappers.neutral_mapper import to_neutral_dict
from app.core.exception import raise_graphql_error
from app.domain.services.endereco_service import EnderecoService
from app.infraestructure.database.repositories.endereco_repository_impl import EnderecoRepositoryImpl
from app.presentation.graphql.inputs.endereco_input import EnderecoFilterInput, EnderecoOrderInput
from app.presentation.graphql.mappers.pagination_mapper import map_pagination
from app.application.validators.schema_validator import validate_schema
from app.presentation.graphql.schemas.endereco_schema import EnderecoInputSchema, EnderecoOrderSchema
from app.presentation.graphql.types.endereco_type import PaginatedResponseEnderecoListType
from app.presentation.graphql.types.pagination_type import PaginationType


@strawberry.type
class EnderecoQuery:

    @strawberry.field
    async def get_list(
        self,
        info: Info,
        offset: int | None = None,
        limit: int | None = None,
        filter: EnderecoFilterInput | None = None,
        order: EnderecoOrderInput | None = None
    ) -> PaginatedResponseEnderecoListType:
        try:
            neutral_filter = to_neutral_dict(obj=filter)
            validate_schema(
                data=neutral_filter,
                schema=EnderecoInputSchema
            )

            neutral_order = to_neutral_dict(obj=order)
            validate_schema(
                data=neutral_order,
                schema=EnderecoOrderSchema
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
