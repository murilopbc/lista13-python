import xml.etree.ElementTree as ET

# Crie o elemento raiz
elementos_quimicos = ET.Element("elementos_quimicos")

# Elemento para o Hidrogênio
elemento_hidrogenio = ET.Element("elemento")
nome_hidrogenio = ET.Element("nome")
nome_hidrogenio.text = "Hidrogênio"

elemento_hidrogenio.append(nome_hidrogenio)

# Elemento para o Oxigênio
elemento_oxigenio = ET.Element("elemento")
nome_oxigenio = ET.Element("nome")
nome_oxigenio.text = "Oxigênio"

elemento_oxigenio.append(nome_oxigenio)

# Adicione os elementos à raiz
elementos_quimicos.append(elemento_hidrogenio)
elementos_quimicos.append(elemento_oxigenio)

# Crie uma árvore XML
tree = ET.ElementTree(elementos_quimicos)

# Salve o arquivo XML
tree.write("elementos.xml", encoding='utf-8')
