import strawberry
from typing import List
from app.database import fetch_all
from app.schema.types.endereco_type import EnderecoType


@strawberry.type
class EnderecoQuery:
    @strawberry.field
    async def get_enderecos(self, limit: int = 50) -> List[EnderecoType]:
        sql = """
            SELECT id_endereco, logradouro, municipio, uf
            FROM NOTA_FISCAL.ENDERECO
            WHERE ROWNUM <= :limit
            ORDER BY id_endereco
        """
        enderecos = fetch_all(sql, {"limit": limit})
        return [EnderecoType(**e) for e in enderecos]

