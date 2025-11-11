import strawberry
from typing import Optional


@strawberry.type
class EnderecoType:
    id_endereco: Optional[int]
    logradouro: Optional[str]
    municipio: Optional[str]
    uf: Optional[str]

def map_row_to_endereco(row: dict) -> EnderecoType:
    """Converte dicionário do Oracle para objeto Endereco."""
    return EnderecoType(
        id_endereco=row.get("id_endereco"),
        logradouro=row.get("logradouro"),
        municipio=row.get("municipio"),
        uf=row.get("uf")
    )
