# Ecommerce Insights

Este projeto tem como objetivo realizar **análise exploratória e visualização de dados** de um e-commerce fictício.  
A base de dados utilizada é `ecommerce_preparados.csv`, contendo informações sobre produtos, marcas, temporadas, quantidade vendida, número de avaliações e preço.

## 📂 Estrutura do projeto
- `main.py` → script principal com tratamento dos dados e geração dos gráficos.
- `ecommerce_preparados.csv` → base de dados fictícia com 150 produtos.

## 🚀 Funcionalidades
- Leitura e tratamento dos dados com **Pandas**.
- Conversão de variáveis categóricas em códigos numéricos.
- Substituição de valores nulos e padronização de categorias.
- Geração de gráficos com **Matplotlib** e **Seaborn**:
  - Histograma de vendas por temporada.
  - Pairplot para análise multivariada.
  - Mapa de calor de correlação.
  - Gráficos de barras e pizza para distribuição de vendas.
  - Gráfico de regressão para relação entre variáveis.

## 🛠️ Tecnologias utilizadas
- Python 3.14
- Pandas
- Matplotlib
- Seaborn

## 📊 Objetivo
Fornecer insights visuais sobre o comportamento das vendas em diferentes temporadas e marcas, apoiando análises exploratórias e decisões estratégicas.

## ▶️ Como executar
1. Instale as dependências:
   ```bash
   python -m pip install pandas matplotlib seaborn
