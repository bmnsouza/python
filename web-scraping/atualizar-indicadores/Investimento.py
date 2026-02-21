import time
from datetime import datetime

from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# URL
URL_INVESTIDOR10_ETF = "https://investidor10.com.br/etfs-global"
URL_INVESTIDOR10_FII = "https://investidor10.com.br/fiis"

# HTML
DIV_1 = "/div[1]"
DIV_13 = "/div[13]"
DIV_BODY = "//div[@class='_card-body']"
DIV_COTACAO = "//div[@class='_card cotacao']"
DIV_DESC = "//div[@class='desc']"
DIV_DY = "//div[@class='_card dy']"
DIV_ETF = "/div[@class='etfCurrentQuotation']"
DIV_TABLE_INDICATORS = "//div[@id='table-indicators']"
DIV_VALUE = "//div[@class='value']"
SPAN_1 = "/span[1]"

# Outros
ARQUIVO_EXCEL = "Investimento.xlsx"
ABA_PLANILHA = "Indicadores"
LOG_FILE = "log.txt"


def escrever_log(mensagem: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file=LOG_FILE, mode="a", encoding="utf-8") as log:
        log.write(f"{timestamp} - {mensagem}\n")


def configurar_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def converter_moeda(valor: str) -> float:
    return float(
        valor.replace("R$", "")
        .replace("US$", "")
        .replace(".", "")
        .replace(",", ".")
        .strip()
    )


def converter_percentual(valor: str) -> float:
    return float(valor.replace("%", "").replace(",", ".").strip()) / 100


def processar_etfs(driver, worksheet):
    print("*** ETFs ***")
    row = 3

    while True:
        ativo = worksheet.cell(row=row, column=2).value
        if not ativo:
            break

        driver.get(f"{URL_INVESTIDOR10_ETF}/{ativo.lower()}/")
        time.sleep(1)

        try:
            preco = driver.find_element(
                By.XPATH,
                DIV_COTACAO + DIV_BODY + DIV_ETF + SPAN_1,
            ).text.strip()

            dividendo = driver.find_element(
                By.XPATH,
                DIV_DY + DIV_BODY + SPAN_1,
            ).text.strip()

            print(f"{ativo} = Preço: {preco}; Dividendo: {dividendo}")

            worksheet.cell(row=row, column=3).value = converter_moeda(
                valor=preco
            )
            worksheet.cell(row=row, column=4).value = converter_percentual(
                valor=dividendo
            )
        except Exception as e:
            mensagem = f"Erro ao buscar ETF {ativo}: {e}"
            print(mensagem)
            escrever_log(mensagem)
            break

        row += 1


def processar_fiis(driver, worksheet):
    print("\n*** FIIs ***")
    row = 10

    while True:
        ativo = worksheet.cell(row=row, column=2).value
        if not ativo:
            break

        driver.get(f"{URL_INVESTIDOR10_FII}/{ativo.lower()}/")
        time.sleep(1)

        try:
            preco = driver.find_element(
                By.XPATH,
                DIV_COTACAO + DIV_BODY + DIV_1 + SPAN_1,
            ).text.strip()

            vp = driver.find_element(
                By.XPATH,
                DIV_TABLE_INDICATORS + DIV_13 + DIV_DESC + DIV_VALUE,
            ).text.strip()

            dividendo = driver.find_element(
                By.XPATH,
                DIV_DY + DIV_BODY + DIV_1 + SPAN_1,
            ).text.strip()

            print(
                f"{ativo} = Preço: {preco}; VP: {vp}; Dividendo: {dividendo}"
            )

            worksheet.cell(row=row, column=3).value = converter_moeda(
                valor=preco
            )
            worksheet.cell(row=row, column=4).value = converter_moeda(valor=vp)
            worksheet.cell(row=row, column=5).value = converter_percentual(
                valor=dividendo
            )
        except Exception as e:
            mensagem = f"Erro ao buscar FII {ativo}: {e}"
            print(mensagem)
            escrever_log(mensagem)
            break

        row += 1


def main():
    driver = configurar_driver()
    workbook = load_workbook(ARQUIVO_EXCEL)
    worksheet = workbook[ABA_PLANILHA]

    processar_etfs(driver, worksheet)
    processar_fiis(driver, worksheet)

    workbook.save(ARQUIVO_EXCEL)
    driver.quit()

    print("\nPlanilha atualizada com sucesso.")
    time.sleep(5)


if __name__ == "__main__":
    main()
