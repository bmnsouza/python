from collections import defaultdict
from typing import Iterable, Optional, Set, Type
from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeMeta


def validate_fields_param(
    fields: Optional[str],
    *,
    orm_model: Optional[DeclarativeMeta] = None,
    schema: Optional[Type[BaseModel]] = None,
) -> Optional[Set[str]]:
    if not fields:
        return None

    if not orm_model and not schema:
        raise ValueError("Informe orm_model ou schema")

    requested = {f.strip() for f in fields.split(",")}

    valid_fields: Set[str] = set()

    # 🔹 Caso ORM
    if orm_model:
        # Campos da tabela
        valid_fields |= set(orm_model.__table__.columns.keys())

        # Relacionamentos
        for rel_name, rel in orm_model.__mapper__.relationships.items():
            valid_fields.add(rel_name)

            target_model = rel.mapper.class_
            for col in target_model.__table__.columns.keys():
                valid_fields.add(f"{rel_name}.{col}")

    # 🔹 Caso SQL nativo / Schema
    if schema:
        valid_fields |= set(schema.model_fields.keys())

    invalid = requested - valid_fields
    if invalid:
        raise HTTPException(
            status_code=400,
            detail=f"Campos inválidos em fields: {', '.join(sorted(invalid))}"
        )

    return requested


def select_fields_from_obj(obj, fields: Optional[Iterable[str]] = None):
    # Converte para dict preservando ordem
    if hasattr(obj, "model_dump"):
        obj_dict = obj.model_dump()
    elif hasattr(obj, "__table__"):
        obj_dict = {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
    else:
        obj_dict = obj

    if not fields:
        return obj_dict

    # Separa campos diretos e aninhados
    direct_fields = set()
    nested_fields = defaultdict(set)

    for f in fields:
        if "." in f:
            parent, child = f.split(".", 1)
            nested_fields[parent].add(child)
        else:
            direct_fields.add(f)

    result = {}

    # Campos diretos – ordem original do objeto
    for key, value in obj_dict.items():
        if key in direct_fields:
            result[key] = value

    # Relacionamentos – ordem original do objeto
    for key, value in obj_dict.items():
        if key not in nested_fields:
            continue

        subfields = nested_fields[key]

        if value is None:
            continue

        if isinstance(value, list):
            result[key] = [
                {k: v for k, v in item.items() if k in subfields}
                for item in value
            ]
        elif isinstance(value, dict):
            result[key] = {k: v for k, v in value.items() if k in subfields}

    return result
