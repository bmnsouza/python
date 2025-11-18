# GraphQL API e FastAPI Notas Fiscais
API de consulta a dados de Notas Fiscais construída com **FastAPI**, **Strawberry GraphQL** e **Oracle** usando SQLAlchemy ORM e SQL Nativo.

---

## Estrutura do Projeto
```bash
notas_fiscais_orm_sql/
├── .vscode/
│   ├── launch.json
│   ├── settings.json
├── app/
│   ├── core/
│   |   ├── __init__.py
│   |   ├── config.py
│   |   ├── constants.py
│   |   └── context.py
│   ├── crud/
│   |   ├── __init__.py
│   |   ├── contribuinte_crud.py
│   |   ├── danfe_crud.py
│   |   └── endereco_crud.py
│   ├── fastapi/
│   |   ├── crud/
│   |   |   ├── __init__.py
│   |   |   ├── contribuinte_crud.py
│   |   |   ├── danfe_crud.py
│   |   |   └── endereco_crud.py
│   |   ├── routers/
│   |   |   ├── __init__.py
│   |   |   ├── contribuinte_router.py
│   |   |   ├── danfe_router.py
│   |   |   └── endereco_router.py
│   |   ├── schemas/
│   |   |   ├── __init__.py
│   |   |   ├── contribuinte_schema.py
│   |   |   ├── danfe_schema.py
│   |   |   └── endereco_schema.py
│   ├── graphql/
│   |   ├── schemas/
│   |   |   ├── mutation/
│   |   |   |   ├── __init__.py
│   |   |   |   ├── contribuinte_mutation.py
│   |   |   |   ├── danfe_mutation.py
│   |   |   |   └── endereco_mutation.py
│   |   |   ├── query/
│   |   |   |   ├── __init__.py
│   |   |   |   ├── contribuinte_query.py
│   |   |   |   ├── danfe_query.py
│   |   |   |   └── endereco_query.py
│   |   |   ├── types/
│   |   |   |   ├── __init__.py
│   |   |   |   ├── contribuinte_type.py
│   |   |   |   ├── danfe_type.py
│   |   |   |   └── endereco_type.py
│   |   └── __init__.py
│   ├── middleware/
│   |   ├── logging_middleware.py
│   |   └── sql_audit_middleware.py
│   ├── models/
│   |   ├── contribuinte_model.py
│   |   ├── danfe_model.py
│   |   └── endereco_model.py
│   ├── utils/
│   |   └── pagination.py
│   ├── __init__.py
│   ├── config.py
│   ├── context.py
│   ├── database.py
│   ├── logger.py
│   └── main.py
├── logs/
│   ├── app.log
│   └── sql.log
├── sql/
│   ├── script.sql
│   └── setup.sql
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Requisitos
- Python 3.13.3
- Oracle Client / Instant Client configurado
- Banco de dados Oracle 11g ou superior
- Pacotes Python (ver `requirements.txt`)

---

## Instalação
```bash
pip install -r requirements.txt
```

---

## Iniciar servidor
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```
