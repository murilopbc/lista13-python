import openpyxl
import csv

# Abre o arquivo XLSX
planilha_xlsx = openpyxl.load_workbook("historico_pedidos.xlsx")

# Seleciona a planilha desejada (por exemplo, a primeira planilha)
planilha_ativa = planilha_xlsx.active

# Cria um arquivo CSV para escrita
with open("historico_pedidos.csv", "w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    # Itera pelas linhas da planilha e escreve no arquivo CSV
    for linha in planilha_ativa.iter_rows(values_only=True):
        escritor_csv.writerow(linha)
