import strawberry
from typing import Optional
from app.database import get_pool
from app.logger import log_sql
from app.schema.types.endereco_type import EnderecoType


@strawberry.type
class EnderecoMutation:
    @strawberry.mutation
    async def criar_endereco(
        self,
        cd_contribuinte: str,
        logradouro: str,
        municipio: str,
        uf: str
    ) -> EnderecoType:
        sql = """
            INSERT INTO NOTA_FISCAL.ENDERECO
                (cd_contribuinte, logradouro, municipio, uf)
            VALUES (:cd, :log, :mun, :uf)
            RETURNING id_endereco INTO :id
        """

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                id_out = cursor.var(int)
                cursor.execute(sql, {
                    "cd": cd_contribuinte,
                    "log": logradouro,
                    "mun": municipio,
                    "uf": uf,
                    "id": id_out
                })
                conn.commit()
                id_endereco = id_out.getvalue()[0] if id_out.getvalue() else None

        log_sql(sql, {"cd": cd_contribuinte, "log": logradouro, "mun": municipio, "uf": uf}, 0)
        return EnderecoType(id_endereco=id_endereco, logradouro=logradouro, municipio=municipio, uf=uf)

    @strawberry.mutation
    async def atualizar_endereco(
        self,
        id_endereco: int,
        novo_logradouro: str,
        novo_municipio: str,
        nova_uf: str
    ) -> str:
        sql = """
            UPDATE NOTA_FISCAL.ENDERECO
            SET logradouro = :logradouro, municipio = :municipio, uf = :uf
            WHERE id_endereco = :id
        """

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, {"logradouro": novo_logradouro, "municipio": novo_municipio, "uf": nova_uf, "id": id_endereco})
                rowcount = cursor.rowcount
                conn.commit()

        log_sql(sql, {"id": id_endereco, "logradouro": novo_logradouro, "municipio": novo_municipio, "uf": nova_uf}, 0)
        if rowcount == 0:
            return f"Endereço {id_endereco} não encontrado."
        return f"Endereço {id_endereco} atualizado com sucesso."

    @strawberry.mutation
    async def excluir_endereco(self, id_endereco: int) -> str:
        sql = "DELETE FROM NOTA_FISCAL.ENDERECO WHERE id_endereco = :id"

        pool = get_pool()
        with pool.acquire() as conn:
            with conn.cursor() as cursor:
                cursor.execute(sql, {"id": id_endereco})
                rowcount = cursor.rowcount
                conn.commit()

        log_sql(sql, {"id": id_endereco}, 0)
        if rowcount == 0:
            return f"Endereço {id_endereco} não encontrado."
        return f"Endereço {id_endereco} excluído com sucesso."
