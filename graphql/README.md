# GraphQL
Estudos de GraphQL.

---

### Pré-requisitos

- Python 3.13.3
- Oracle Client / Instant Client configurado
- Banco de dados Oracle 11g ou superior
- Pacotes Python (ver `requirements.txt`)

---

### Instalação Local

1. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute a aplicação**:
   ```bash
   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8080
   ```

A aplicação estará disponível em `http://localhost:8080`
