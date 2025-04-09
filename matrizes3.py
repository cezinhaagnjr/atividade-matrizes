import pandas as pd
dados = {
    "Nome": ["Alice", "Bob", "César"],
    "Idade": [25,30,35],
    "Cidade": ["São Paulo","Rio de Janeiro","Curitiba"]
}

df = pd.DataFrame(dados)
print(df)