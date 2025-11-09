import strawberry
from typing import Optional
from app.database import get_pool
from app.logger import log_sql
from app.schema.types.contribuinte_type import ContribuinteType


@strawberry.type
class ContribuinteMutation:
    @strawberry.mutation
    async def criar_contribuinte(
        self,
        cd_contribuinte: str,
        nm_fantasia: Optional[str],
        cnpj_contribuinte: str
    ) -> ContribuinteType:
        sql = """
            INSERT INTO NOTA_FISCAL.CONTRIBUINTE
                (cd_contribuinte, nm_fantasia, cnpj_contribuinte)
            VALUES (:cd, :nm, :cnpj)
        """

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, {
                    "cd": cd_contribuinte,
                    "nm": nm_fantasia,
                    "cnpj": cnpj_contribuinte
                })
                conn.commit()

        log_sql(sql, {"cd": cd_contribuinte, "nm": nm_fantasia, "cnpj": cnpj_contribuinte}, 0)
        return ContribuinteType(cd_contribuinte=cd_contribuinte, nm_fantasia=nm_fantasia, cnpj_contribuinte=cnpj_contribuinte)

    @strawberry.mutation
    async def atualizar_contribuinte(
        self,
        cd_contribuinte: str,
        nova_fantasia: str
    ) -> str:
        sql = """
            UPDATE NOTA_FISCAL.CONTRIBUINTE
            SET nm_fantasia = :fantasia
            WHERE cd_contribuinte = :cd
        """

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, {"fantasia": nova_fantasia, "cd": cd_contribuinte})
                rowcount = cursor.rowcount
                conn.commit()

        log_sql(sql, {"cd": cd_contribuinte, "fantasia": nova_fantasia}, 0)
        if rowcount == 0:
            return f"Contribuinte {cd_contribuinte} não encontrado."
        return f"Contribuinte {cd_contribuinte} atualizado com sucesso."

    @strawberry.mutation
    async def excluir_contribuinte(self, cd_contribuinte: str) -> str:
        sql = "DELETE FROM NOTA_FISCAL.CONTRIBUINTE WHERE cd_contribuinte = :cd"

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, {"cd": cd_contribuinte})
                rowcount = cursor.rowcount
                conn.commit()

        log_sql(sql, {"cd": cd_contribuinte}, 0)
        if rowcount == 0:
            return f"Contribuinte {cd_contribuinte} não encontrado."
        return f"Contribuinte {cd_contribuinte} excluído com sucesso."
