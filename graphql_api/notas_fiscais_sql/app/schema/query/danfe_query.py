import strawberry
from typing import List, Optional
from app.database import fetch_all, fetch_one
from app.schema.types.danfe_type import DanfeType, FiltroDanfeInput, PaginacaoDanfe


@strawberry.type
class DanfeQuery:
    @strawberry.field
    async def get_danfes(self, limit: int = 50) -> List[DanfeType]:
        sql = """
            SELECT id_danfe, numero, valor_total, data_emissao, cd_contribuinte
            FROM NOTA_FISCAL.DANFE
            WHERE ROWNUM <= :limit
            ORDER BY data_emissao DESC
        """
        danfes = fetch_all(sql, {"limit": limit})
        return [DanfeType(**d) for d in danfes]

    @strawberry.field
    async def get_danfes_filtradas(
        self,
        filtro: Optional[FiltroDanfeInput] = None,
        cursor: Optional[int] = None,
        limite: int = 50
    ) -> PaginacaoDanfe:
        """
        Retorna DANFEs com filtros e paginação cursor-based.
        """
        base_sql = """
            SELECT id_danfe, numero, valor_total, data_emissao, cd_contribuinte
            FROM NOTA_FISCAL.DANFE
            WHERE 1=1
        """
        params = {}

        if filtro:
            if filtro.numero:
                base_sql += " AND numero = :num"
                params["num"] = filtro.numero
            if filtro.valor_minimo is not None:
                base_sql += " AND valor_total >= :vmin"
                params["vmin"] = filtro.valor_minimo
            if filtro.valor_maximo is not None:
                base_sql += " AND valor_total <= :vmax"
                params["vmax"] = filtro.valor_maximo
            if filtro.data_inicial:
                base_sql += " AND data_emissao >= :dini"
                params["dini"] = filtro.data_inicial
            if filtro.data_final:
                base_sql += " AND data_emissao <= :dfim"
                params["dfim"] = filtro.data_final
            if filtro.cd_contribuinte:
                base_sql += " AND cd_contribuinte = :cd"
                params["cd"] = filtro.cd_contribuinte

        if cursor:
            base_sql += " AND id_danfe > :cursor"
            params["cursor"] = cursor

        base_sql += " ORDER BY id_danfe FETCH FIRST :limite ROWS ONLY"
        params["limite"] = limite

        danfes = fetch_all(base_sql, params)
        total = fetch_one("SELECT COUNT(*) AS qtd FROM NOTA_FISCAL.DANFE")
        total_registros = total["qtd"] if total else 0
        proximo_cursor = danfes[-1]["id_danfe"] if danfes else None

        return PaginacaoDanfe(
            total_registros=total_registros,
            proximo_cursor=proximo_cursor,
            danfes=[DanfeType(**d) for d in danfes]
        )
