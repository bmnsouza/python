from typing import List, Optional
import strawberry
from sqlalchemy import select, text
from sqlalchemy.orm import selectinload
from app.models.contribuinte_model import ContribuinteModel
from app.graphql.schemas.types.contribuinte_type import ContribuinteType, ContribuinteDenfeEndereoType, PaginatedType
from app.utils.pagination import calculate_offset
from app.core.constants import DEFAULT_PAGE_SIZE


@strawberry.type
class ContribuinteQuery:

    @strawberry.field
    async def get_contribuintes_danfe_endereco(self, info, filtro_nome: str, page: int = 1) -> PaginatedType:
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
        data = [ContribuinteDenfeEndereoType(**row) for row in rows]
        return PaginatedType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)


    @strawberry.field
    async def get_contribuintes_paginado(self, info, page: int = 1) -> PaginatedType:
        """Retorna contribuintes paginados (usando ORM e função paginate_query)."""
        session = info.context["session"]
        query = (
            select(ContribuinteModel)
            .options(
                selectinload(ContribuinteModel.danfes),
                selectinload(ContribuinteModel.enderecos)
            )
            .order_by(ContribuinteModel.nm_fantasia)
            .offset(calculate_offset(page))
            .limit(DEFAULT_PAGE_SIZE)
        )

        result = await session.execute(query)
        contribuintes = result.scalars().unique().all()
        data = [ContribuinteType.from_orm(c) for c in contribuintes]
        return PaginatedType(page=page, page_size=DEFAULT_PAGE_SIZE, data=data)


    @strawberry.field
    async def get_contribuintes(self, info, limit: int = 10) -> List[ContribuinteType]:
        """Retorna uma lista de contribuintes com endereços e danfes."""
        session = info.context["session"]
        result = await session.execute(
            select(ContribuinteModel)
            .options(
                selectinload(ContribuinteModel.danfes),
                selectinload(ContribuinteModel.enderecos)
            )
            .order_by(ContribuinteModel.nm_fantasia)
            .limit(limit)
        )
        contribuintes = result.scalars().unique().all()
        return [ContribuinteType.from_orm(c) for c in contribuintes]


    @strawberry.field
    async def get_contribuinte_por_cnpj(self, info, cnpj: str) -> Optional[ContribuinteType]:
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
