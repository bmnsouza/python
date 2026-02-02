# Notas Fiscais
Projeto de Notas Fiscais construído com **GraphQL** e **Oracle**.

---

### Pré-requisitos

- Python 3.13.3
- Oracle Client / Instant Client configurado
- Banco de dados Oracle 11g ou superior
- Pacotes Python (ver `requirements.txt`)

---

### Instalação Local

1. **Crie um ambiente virtual**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**:
   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8080
   ```

A aplicação estará disponível em `http://localhost:8080`

---

### Estrutura do Projeto

```bash
notas_fiscais/
├── .vscode/
│   ├── launch.json
│   └── settings.json
├── app/
│   ├── application/
│   |   ├── dto/
│   |   |   ├── contribuinte_danfe_dto.py
│   |   |   ├── contribuinte_dto.py
│   |   |   ├── danfe_dto.py
│   |   |   └── endereco_dto.py
│   |   ├── mappers/
│   |   |   └── neutral_mapper.py
│   |   └── validators/
│   |       └── schema_validator.py
│   ├── core/
│   |   ├── config.py
│   |   ├── constants.py
│   |   └── exception.py
│   ├── domain/
│   |   ├── repositories/
│   |   |   ├── contribuinte_danfe_repository.py
│   |   |   ├── contribuinte_repository.py
│   |   |   ├── danfe_repository.py
│   |   |   └── endereco_repository.py
│   |   ├── services/
│   |   |   ├── contribuinte_danfe_service.py
│   |   |   ├── contribuinte_service.py
│   |   |   ├── danfe_service.py
│   |   |   └── endereco_service.py
│   |   └── values/
│   |       ├── contribuinte_value.py
│   |       └── data_value.py
│   ├── infraestructure/
│   |   └── database/
│   |       ├── models.py
│   |       |   ├── contribuinte_model.py
│   |       |   ├── danfe_model.py
│   |       |   └── endereco_model.py
│   |       ├── query.py
│   |       |   ├── order_by_builder.py
│   |       |   └── pagination_builder.py
│   |       ├── repositories.py
│   |       |   ├── contribuinte_danfe_repository_impl.py
│   |       |   ├── contribuinte_repository_impl.py
│   |       |   ├── danfe_repository_impl.py
│   |       |   └── endereco_repository_impl.py
│   |       ├── connection.py
│   |       ├── context.py
│   |       └── session.py
│   └── presentation/
│       └── graphql/
│           ├── inputs/
│           |   ├── contribuinte_danfe_input.py
│           |   ├── contribuinte_input.py
│           |   ├── danfe_input.py
│           |   ├── endereco_input.py
│           |   └── order_input.py
│           ├── mappers/
│           |   └── pagination_mapper.py
│           ├── resolvers/
│           |   ├── contribuinte_danfe_resolver.py
│           |   ├── contribuinte_resolver.py
│           |   ├── danfe_resolver.py
│           |   └── endereco_resolver.py
│           ├── types/
│           |   ├── contribuinte_danfe_type.py
│           |   ├── contribuinte_type.py
│           |   ├── danfe_type.py
│           |   ├── endereco_type.py
│           |   └── pagination_type.py
│           ├── validators/
│           |   ├── contribuinte_danfe_validator.py
│           |   ├── contribuinte_validator.py
│           |   ├── danfe_validator.py
│           |   └── endereco_validator.py
│           └── graphql_router.py
├── sql/
│   ├── script.sql
│   └── setup.sql
├── .env
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```
