with open('aula.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write("Python é legal!\nAprendendo manipulação de arquivos")
with open('aula.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read())
