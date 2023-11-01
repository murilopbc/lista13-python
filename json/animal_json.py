import json

dados = {
    "Cachorro": "Rex",
    "Gato": "Felix",
}
with open('info.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)
with open('info.json', 'r') as arquivo:
    dados = json.load(arquivo)
    print(dados)
