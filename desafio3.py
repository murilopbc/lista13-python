import csv
import json


csv_file = 'historico_pedidos.csv'
json_file = 'historico_pedidos.json'

dados = []

with open(csv_file, 'r', newline='') as csvfile:
    file = csv.DictReader(csvfile)
    for linha in file:
        dados.append(linha)
with open(json_file, 'w', encoding='utf-8') as jsonfile:
    json.dump(dados, jsonfile, ensure_ascii=False, indent=4)
