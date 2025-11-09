import strawberry
from typing import List, Optional
from app.database import fetch_all
from app.schema.types.contribuinte_type import ContribuinteType
from app.schema.types.danfe_type import DanfeType
from app.schema.types.endereco_type import EnderecoType


@strawberry.type
class ContribuinteQuery:
    @strawberry.field
    async def get_contribuintes(self, limit: int = 10) -> List[ContribuinteType]:
        sql = """
            SELECT cd_contribuinte, nm_fantasia, cnpj_contribuinte
            FROM NOTA_FISCAL.CONTRIBUINTE
            WHERE ROWNUM <= :limit
        """
        contribs = fetch_all(sql, {"limit": limit})
        contribuintes_result = []

        for c in contribs:
            enderecos_db = fetch_all(
                "SELECT id_endereco, logradouro, municipio, uf FROM NOTA_FISCAL.ENDERECO WHERE cd_contribuinte = :cd",
                {"cd": c["cd_contribuinte"]}
            )
            danfes_db = fetch_all(
                "SELECT id_danfe, numero, valor_total, data_emissao FROM NOTA_FISCAL.DANFE WHERE cd_contribuinte = :cd",
                {"cd": c["cd_contribuinte"]}
            )

            c["enderecos"] = [EnderecoType(**e) for e in enderecos_db]
            c["danfes"] = [DanfeType(**d) for d in danfes_db]
            contribuintes_result.append(ContribuinteType(**c))

        return contribuintes_result

    @strawberry.field
    async def get_contribuinte_por_cnpj(self, cnpj: str) -> Optional[ContribuinteType]:
        sql = """
            SELECT cd_contribuinte, nm_fantasia, cnpj_contribuinte
            FROM NOTA_FISCAL.CONTRIBUINTE
            WHERE cnpj_contribuinte = :cnpj
        """
        result = fetch_all(sql, {"cnpj": cnpj})
        if not result:
            return None

        c = result[0]
        enderecos_db = fetch_all(
            "SELECT id_endereco, logradouro, municipio, uf FROM NOTA_FISCAL.ENDERECO WHERE cd_contribuinte = :cd",
            {"cd": c["cd_contribuinte"]}
        )
        danfes_db = fetch_all(
            "SELECT id_danfe, numero, valor_total, data_emissao FROM NOTA_FISCAL.DANFE WHERE cd_contribuinte = :cd",
            {"cd": c["cd_contribuinte"]}
        )

        c["enderecos"] = [EnderecoType(**e) for e in enderecos_db]
        c["danfes"] = [DanfeType(**d) for d in danfes_db]
        return ContribuinteType(**c)
