import pandas as pd

df = pd.DataFrame({
    "Nome": ["Murilo", "Caio"],
    "Matemática": [9, 10],
    "Português": [7, 8]
})

df.to_excel("notas.xlsx", index=False)

df = pd.read_excel("notas.xlsx")
print(df)
