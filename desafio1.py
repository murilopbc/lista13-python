import pandas as pd

df = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Nome": ["João", "Mariana", "Carlos", "Fernanda"],
    "Endereço": ["Rua das Flores, 123", "Avenida Central, 456", "Praça da Estação, 789", "Alameda dos Anjos, 101"],
    "Produto": ["Camiseta", "Tênis", "Mochila", "Relógio"],
    "Quantidade": [2, 1, 1, 1],
    "Preço": [50, 120, 80, 150],
    "Data": ["01/01/2023", "02/01/2023", "03/01/2023", "04/01/2023"]
})
df.to_excel("historico_pedidos.xlsx", index=False)

df = pd.read_excel("historico_pedidos.xlsx")
print(df)
