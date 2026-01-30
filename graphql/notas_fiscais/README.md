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
