from typing import Optional
import strawberry
from strawberry.types import Info
from sqlalchemy import select, text
from sqlalchemy.orm import selectinload
from app.model.contribuinte_model import ContribuinteModel
from app.graphql.schema.type.contribuinte_type import ContribuinteType, ContribuinteDenfeEnderecoType, PaginatedType
from app.core.pagination import DEFAULT_PAGE, DEFAULT_PAGE_SIZE, calculate_offset
from app.service import contribuinte_service


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_contribuintes_danfe_endereco(self, info: Info, filtro_nome: str, page: int = DEFAULT_PAGE) -> PaginatedType:
        print("filtro_nome:", filtro_nome)
        session = info.context["session"]
        query = text("""
            SELECT c.CD_CONTRIBUINTE, c.CNPJ_CONTRIBUINTE, c.NM_FANTASIA,
                d.NUMERO, TO_CHAR(d.DATA_EMISSAO, 'dd/mm/yyyy') AS DATA_EMISSAO, d.VALOR_TOTAL,
                e.LOGRADOURO, e.MUNICIPIO, e.UF
            FROM NOTA_FISCAL.CONTRIBUINTE c JOIN NOTA_FISCAL.DANFE d ON d.CD_CONTRIBUINTE = c.CD_CONTRIBUINTE
            JOIN NOTA_FISCAL.ENDERECO e  ON e.CD_CONTRIBUINTE = c.CD_CONTRIBUINTE
            WHERE c.NM_FANTASIA LIKE :filtro_nome
            ORDER BY c.NM_FANTASIA, d.DATA_EMISSAO, d.VALOR_TOTAL
            OFFSET :page ROWS FETCH NEXT :page_size ROWS ONLY
        """)

        params = {
            "filtro_nome": f"%{filtro_nome}%",
            "page": calculate_offset(page),
            "page_size": DEFAULT_PAGE_SIZE   
        }

        result = await session.execute(query, params)
        rows = result.mappings().all()
        data = [ContribuinteDenfeEnderecoType(**row) for row in rows]
        return PaginatedType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)


    @strawberry.field
    async def get_contribuintes(self, info: Info, page: int) -> PaginatedType:
        """Retorna contribuintes paginados (usando ORM e função paginate_query)."""
        session = info.context["session"]

        result = await contribuinte_service.get_contribuintes(db=session, page=page)
        data = [ContribuinteType.from_orm(c) for c in result["data"]]

        return PaginatedType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)


    @strawberry.field
    async def get_contribuinte_por_cnpj(self, info: Info, cnpj: str) -> Optional[ContribuinteType]:
        """Busca um contribuinte pelo CNPJ."""
        session = info.context["session"]
        result = await session.execute(
            select(ContribuinteModel)
            .options(
                selectinload(ContribuinteModel.danfes),
                selectinload(ContribuinteModel.enderecos)
            )
            .where(ContribuinteModel.cnpj_contribuinte == cnpj)
        )
        contrib = result.scalars().first()
        return ContribuinteType.from_orm(contrib) if contrib else None
