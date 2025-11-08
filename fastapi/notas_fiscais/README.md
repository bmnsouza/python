# FastAPI Notas Fiscais

API de consulta a dados de Notas Fiscais construída com **FastAPI** e **Oracle**.

## Estrutura
- app/
  - crud
    - contribuinte_crud.py
    - danfe_crud.py
    - endereco_crud.py
  - models.py
    - contribuinte_model.py
    - danfe_model.py
    - endereco_model.py
  - routers
    - contribuinte_router.py
    - danfe_router.py
    - endereco_router.py
  - schemas
    - contribuinte_schema.py
    - danfe_schema.py
    - endereco_schema.py
  - config.py
  - database.py
  - main.py
- sql
  - script.sql
  - setup.sql
- .env
- .gitignore
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
