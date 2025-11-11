import strawberry
from app.database import get_pool
from app.logger import log_sql
from app.schema.types.danfe_type import DanfeType


@strawberry.type
class DanfeMutation:
    @strawberry.mutation
    async def criar_danfe(
        self,
        cd_contribuinte: str,
        numero: str,
        valor_total: float
    ) -> DanfeType:
        sql = """
            INSERT INTO NOTA_FISCAL.DANFE
                (cd_contribuinte, numero, valor_total, data_emissao)
            VALUES (:cd, :num, :valor, SYSDATE)
            RETURNING id_danfe, data_emissao INTO :id, :data
        """

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                id_out = cursor.var(int)
                data_out = cursor.var(str)
                cursor.execute(sql, {
                    "cd": cd_contribuinte,
                    "num": numero,
                    "valor": valor_total,
                    "id": id_out,
                    "data": data_out
                })
                conn.commit()
                id_danfe = id_out.getvalue()[0] if id_out.getvalue() else None
                data_emissao = data_out.getvalue()[0] if data_out.getvalue() else None

        log_sql(sql, {"cd": cd_contribuinte, "num": numero, "valor": valor_total}, 0)
        return DanfeType(
            id_danfe=id_danfe,
            numero=numero,
            valor_total=valor_total,
            data_emissao=data_emissao,
            cd_contribuinte=cd_contribuinte
        )

    @strawberry.mutation
    async def atualizar_danfe(
        self,
        id_danfe: int,
        novo_numero: str,
        novo_valor: float
    ) -> str:
        sql = """
            UPDATE NOTA_FISCAL.DANFE
            SET numero = :numero, valor_total = :valor
            WHERE id_danfe = :id
        """

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, {"numero": novo_numero, "valor": novo_valor, "id": id_danfe})
                rowcount = cursor.rowcount
                conn.commit()

        log_sql(sql, {"id": id_danfe, "numero": novo_numero, "valor": novo_valor}, 0)
        if rowcount == 0:
            return f"DANFE {id_danfe} não encontrado."
        return f"DANFE {id_danfe} atualizado com sucesso."

    @strawberry.mutation
    async def excluir_danfe(self, id_danfe: int) -> str:
        sql = "DELETE FROM NOTA_FISCAL.DANFE WHERE id_danfe = :id"

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, {"id": id_danfe})
                rowcount = cursor.rowcount
                conn.commit()

        log_sql(sql, {"id": id_danfe}, 0)
        if rowcount == 0:
            return f"DANFE {id_danfe} não encontrado."
        return f"DANFE {id_danfe} excluído com sucesso."
