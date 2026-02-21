# Atualizar Indicadores

Script em **Python** que realiza web scraping no site Investidor10 e atualiza automaticamente a aba **Indicadores** da planilha `Investimento.xlsx`.

O script coleta:

- ETFs globais (preço e dividend yield)
- FIIs (preço, VP e dividend yield)

---

## Tecnologias Utilizadas

- Python 3.13+
- Selenium
- OpenPyXL
- Black (formatação)
- Flake8 (lint)
- isort (organização de imports)

---

## Instalação

O projeto utiliza `pyproject.toml` para gerenciamento de dependências.

### Instalar dependências principais

```bash
pip install .
```

### Instalar dependências opcionais
```bash
pip install .[dev]
```
