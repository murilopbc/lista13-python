# Função para descriptografar uma mensagem com a cifra de César
def descriptografar_cifra_cesar(texto, deslocamento):
    texto_descriptografado = ""
    for caractere in texto:
        if caractere.isalpha():
            deslocamento_mod = deslocamento % 26
            if caractere.islower():
                caractere_descriptografado = chr(((ord(caractere) - ord('a') - deslocamento_mod + 26) % 26) + ord('a'))
            else:
                caractere_descriptografado = chr(((ord(caractere) - ord('A') - deslocamento_mod + 26) % 26) + ord('A'))
        else:
            caractere_descriptografado = caractere
        texto_descriptografado += caractere_descriptografado
    return texto_descriptografado

# Resto do código (leitura do arquivo, descriptografia e escrita do texto descriptografado) permanece o mesmo


# Lê o arquivo criptografado
with open("FPOO-Aula13-ManipulacaoArquivo-Exercicios-Criptografado.txt", "r") as arquivo:
    mensagem_criptografada = arquivo.read()

# Define o deslocamento conhecido (3 na cifra de César)
deslocamento = 3

# Descriptografa a mensagem
mensagem_descriptografada = descriptografar_cifra_cesar(mensagem_criptografada, deslocamento)

# Escreve o texto original em um novo arquivo
with open("descriptografado.txt", "w") as arquivo:
    arquivo.write(mensagem_descriptografada)

print("Mensagem descriptografada e salva em 'descriptografado.txt'.")
