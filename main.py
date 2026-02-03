import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('C:\\Users\\adm\\OneDrive\\Documentos\\codigos\\Projeto de ecommerce\\ecommerce_preparados.csv')
print(df.head().to_string())

# Tratamento
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].fillna(0)
df['Marca'] = df['Marca'].astype('category').cat.codes
# Relação com a Temporada
df['Temporada'] = df['Temporada'].replace('não definido', 'Não Def.')
df['Temporada'] = df['Temporada'].astype('category').cat.codes

# Histograma Temporada x Quantidade de vendas
temporada_vendas = df.groupby('Temporada', observed=True)['Qtd_Vendidos'].sum().sort_values()
plt.figure(figsize=(10, 6))
sns.barplot(
    x=temporada_vendas.index,
    y=temporada_vendas.values,
    hue=temporada_vendas.index,
    palette='viridis',
    legend=False
)
plt.title('Quantidade Total de Vendas por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Total de Vendas')
plt.grid(True, axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pairplot
sns.pairplot(df[['Qtd_Vendidos', 'Marca', 'Temporada', 'N_Avaliações']])
plt.show()

# Mapa de calor
corr = df[['Qtd_Vendidos', 'Temporada', 'Marca', 'N_Avaliações']].corr()
plt.subplot(2, 2, 3)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Vendas')
plt.tight_layout()
plt.show()

# Gráfico de barra
plt.figure(figsize=(10, 6))
df['Qtd_Vendidos'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Vendas realizadas - 1')
plt.xlabel('Vendas')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color='#60aa65')
plt.title('Vendas realizadas - 2')
plt.xlabel('Vendas')
plt.ylabel('Quantidade')

# Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de vendas')
plt.show()

# Gráfico de Regressão
sns.regplot(x='Qtd_Vendidos', y='Temporada', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Quantidade de Vendas')
plt.xlabel('Qtd_Vendidos')
plt.ylabel('Temporada')
plt.show()