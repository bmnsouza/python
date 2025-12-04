from typing import Any, Dict, Optional
from datetime import date, datetime
from sqlalchemy.orm import RelationshipProperty


def format_exception(description: str, code="server_error", title="Internal Server Error"):
    return {
        "errors": [
            {
                "code": code, 
                "title": title, 
                "description": description
            }
        ]
    }

def format_contribuinte(obj) -> Optional[Dict[str, Any]]:
    if obj is None:
        return None

    def fmt_endereco(e):
        return {
            "cd_contribuinte": e.cd_contribuinte,
            "id_endereco": e.id_endereco,
            "logradouro": e.logradouro,
            "municipio": e.municipio,
            "uf": e.uf,
        }

    def fmt_danfe(d):
        return {
            "cd_contribuinte": d.cd_contribuinte,
            "id_danfe": d.id_danfe,
            "numero": d.numero,
            "valor_total": d.valor_total,
            "data_emissao": d.data_emissao.isoformat() if d.data_emissao else None,
        }

    return {
        "cd_contribuinte": obj.cd_contribuinte,
        "nm_fantasia": obj.nm_fantasia,
        "cnpj_contribuinte": obj.cnpj_contribuinte,
        "enderecos": [fmt_endereco(e) for e in (obj.enderecos or [])],
        "danfes": [fmt_danfe(d) for d in (obj.danfes or [])],
    }


def format_sa_model(obj) -> Optional[Dict[str, Any]]:
    """
    Formata automaticamente qualquer SQLAlchemy model usando introspecção.
    Inclui colunas e relações (1..N e 1..1).
    """
    if obj is None:
        return None

    mapper = obj.__class__.__mapper__
    data: Dict[str, Any] = {}

    for attr in mapper.attrs:
        name = attr.key
        value = getattr(obj, name)

        # ------------------------
        # TIPO 1 — coluna comum
        # ------------------------
        if not isinstance(attr, RelationshipProperty):
            if isinstance(value, (datetime, date)):
                data[name] = value.isoformat()
            else:
                data[name] = value
            continue

        # ------------------------
        # TIPO 2 — relacionamento
        # ------------------------
        if value is None:
            data[name] = None
            continue

        if attr.uselist:
            # lista de objetos relacionados
            data[name] = [format_sa_model(child) for child in value]
        else:
            # relacionamento 1:1
            data[name] = format_sa_model(value)

    return data
