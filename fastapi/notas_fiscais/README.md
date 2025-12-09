# FastAPI Notas Fiscais
API de consulta a dados de Notas Fiscais construída com **FastAPI** e **Oracle** usando SQLAlchemy ORM e SQL Nativo.

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
│   |   ├── constants.py
│   |   ├── exceptions.py
│   |   ├── logger.py
│   |   └── pagination.py
│   ├── database/
│   |   ├── __init__.py
│   |   ├── config.py
│   |   ├── connection.py
│   |   ├── context.py
│   |   └── session.py
│   ├── fastapi/
│   |   ├── router/
│   |   |   ├── __init__.py
│   |   |   ├── contribuinte_router.py
│   |   |   ├── danfe_router.py
│   |   |   └── endereco_router.py
│   |   ├── schema/
│   |   |   ├── __init__.py
│   |   |   ├── contribuinte_schema.py
│   |   |   ├── danfe_schema.py
│   |   |   └── endereco_schema.py
│   |   ├── validators/
│   |   |   ├── __init__.py
│   |   |   ├── contribuinte_schema.py
│   |   |   ├── danfe_schema.py
│   |   |   └── endereco_schema.py
|   ├── logs/
│   |   ├── app.log
│   |   └── sql.log
│   ├── middleware/
│   |   ├── logging_middleware.py
│   |   └── sql_audit_middleware.py
│   ├── model/
│   |   ├── contribuinte_model.py
│   |   ├── danfe_model.py
│   |   └── endereco_model.py
│   ├── repository/
│   |   ├── __init__.py
│   |   ├── contribuinte_repository.py
│   |   ├── danfe_repository.py
│   |   ├── endereco_repository.py
│   ├── service/
│   |   ├── __init__.py
│   |   ├── contribuinte_service.py
│   |   ├── danfe_service.py
│   |   └── endereco_service.py
│   ├── utils/
│   |   ├── __init__.py
│   |   ├── error_util.py
│   |   ├── exception_util.py
│   |   ├── field_util.py
│   |   ├── handler_util.py
│   |   └── response_service.py
│   ├── __init__.py
│   └── main.py
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
