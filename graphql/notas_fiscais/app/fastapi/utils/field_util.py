from typing import List, Optional, Set

from fastapi import HTTPException

from sqlalchemy.orm import DeclarativeMeta


def validate_fields_param(fields: Optional[str], model: DeclarativeMeta) -> Optional[Set[str]]:
    if not fields:
        return None

    requested = {f.strip() for f in fields.split(",")}

    # Campos diretos da tabela
    table_fields = set(model.__table__.columns.keys())

    # Relacionamentos ORM
    relationships = model.__mapper__.relationships

    valid_fields = set(table_fields)

    # Campos do tipo relacionamento.campo
    for rel_name, rel in relationships.items():
        target_model = rel.mapper.class_
        target_columns = target_model.__table__.columns.keys()

        valid_fields.add(rel_name)

        for col in target_columns:
            valid_fields.add(f"{rel_name}.{col}")

    invalid = requested - valid_fields
    if invalid:
        raise HTTPException(
            status_code=400,
            detail=f"Campos inválidos em fields: {', '.join(sorted(invalid))}"
        )

    return requested


def select_fields_from_obj(obj, fields: Optional[List[str]] = None):
    # Pydantic v2
    if hasattr(obj, "model_dump"):
        obj_dict = obj.model_dump()
    # SQLAlchemy
    elif hasattr(obj, "__table__"):
        obj_dict = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
    # Já é dict
    else:
        obj_dict = obj

    if not fields:
        return obj_dict

    return {k: v for k, v in obj_dict.items() if k in fields}
