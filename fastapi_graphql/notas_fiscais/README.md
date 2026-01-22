# Notas Fiscais
Projeto de Notas Fiscais construído com **FastAPI**, **GraphQL** e **Oracle**.

---

## Estrutura do Projeto
```bash
notas_fiscais/
├── .vscode/
│   ├── launch.json
│   ├── settings.json
├── app/
│   ├── core/
│   |   ├── exception/
│   |   |   ├── core_exception.py
│   |   |   ├── graphql_exception.py
│   |   |   └── rest_exception.py
│   |   ├── handler/
│   |   |   └── rest_handler.py
│   |   ├── response/
│   |   |   ├── core_response.py
│   |   |   ├── graphql_response.py
│   |   |   └── rest_response.py
│   |   ├── constants.py
│   |   ├── logger.py
│   ├── database/
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
│   ├── graphql/
│   |   ├── input/
│   |   |   ├── contribuinte_input.py
│   |   |   ├── danfe_input.py
│   |   |   ├── endereco_input.py
│   |   |   └── graphql_input.py
│   |   ├── query/
│   |   |   ├── __init__.py
│   |   |   ├── contribuinte_query.py
│   |   |   ├── danfe_query.py
│   |   |   └── endereco_query.py
│   |   ├── type/
│   |   |   ├── contribuinte_type.py
│   |   |   ├── danfe_type.py
│   |   |   └── endereco_type.py
│   |   ├── utils/
│   |   |   ├── exception_util.py
│   |   |   └── response_util.py
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
│   |   ├── contribuinte_repository.py
│   |   ├── danfe_repository.py
│   |   └── endereco_repository.py
│   ├── schema/
│   |   ├── contribuinte_schema.py
│   |   ├── danfe_schema.py
│   |   └── endereco_schema.py
│   ├── service/
│   |   ├── contribuinte_service.py
│   |   ├── danfe_service.py
│   |   └── endereco_service.py
│   ├── validator/
│   |   ├── contribuinte_validator.py
│   |   ├── danfe_validator.py
│   |   └── endereco_validator.py
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
