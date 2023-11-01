import csv

# Escrevendo os dados no arquivo CSV
with open('alunos.csv', 'w', newline='') as csvfile:
    file = csv.writer(csvfile)
    file.writerow(["João", "20 anos"])
    file.writerow(["Maria", "22 anos"])

# Lendo os dados do arquivo CSV
with open('alunos.csv', 'r', newline='') as csvfile:
    file = csv.reader(csvfile)
    for linha in file:
        print(linha)
