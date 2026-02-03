import pandas as pd
import random

produtos = []
marcas = ["Nike", "Adidas", "Levi's", "Zara", "H&M", "GAP", "Mango", "Lacoste", "Arezzo", "Renner",
          "Samsung", "Apple", "Dell", "Lenovo", "Novatec", "Garmin", "Sony", "LG", "Microsoft", "Amazon"]
temporadas = ["Verão", "Inverno", "Outono", "Primavera", "Não Def."]

for i in range(150):
    produto = f"Produto_{i+1}"
    marca = random.choice(marcas)
    temporada = random.choice(temporadas)
    qtd_vendidos = random.randint(10, 300)
    n_avaliacoes = random.randint(5, 150)
    preco = round(random.uniform(50, 3500), 2)
    produtos.append([produto, marca, temporada, qtd_vendidos, n_avaliacoes, preco])

df = pd.DataFrame(produtos, columns=["Produto", "Marca", "Temporada", "Qtd_Vendidos", "N_Avaliações", "Preço"])
df.to_csv("ecommerce_preparados.csv", index=False)
print(df.head())
