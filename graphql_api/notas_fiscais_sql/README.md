# GraphQL API Notas Fiscais

API de consulta a dados de Notas Fiscais construída com **FastAPI**, **Strawberry GraphQL** e **Oracle**.

---

## Estrutura
- app/
  - schema/
    - mutation/
      - contribuinte_mutation.py
      - danfe_mutation.py
      - endereco_mutation.py
    - query/
      - contribuinte_query.py
      - danfe_query.py
      - endereco_query.py
    - types/
      - contribuinte_type.py
      - danfe_type.py
      - endereco_type.py
  - config.py
  - database.py
  - logger.py
  - main.py
- logs/
  - app.log
  - sql.log
- sql/
  - script.sql
  - setup.sql
- tests/
  - test_query.py
- .env
- .gitignore
- pytest.ini
- README.md
- requirements.txt

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
