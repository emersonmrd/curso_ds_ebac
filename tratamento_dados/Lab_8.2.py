import pandas as pd

df = pd.read_csv('/data/ecommerce_ex2.csv')

# Escreva seu código abaixo

# Converter a coluna 'Marca' para letras minúsculas
df['Marca'] = df['Marca'].str.lower()

# Converter a coluna 'Material' para letras minúsculas
df['Material'] = df['Material'].str.lower()

# Converter a coluna 'Temporada' para letras minúsculas
df['Temporada'] = df['Temporada'].str.lower()

# Remover linhas duplicadas
df = df.dropna(thresh=8)

# Remover linhas com menos de 8 valores não nulos
# O parâmetro 'thresh' define o número mínimo de valores não nulos necessários para manter a linha
...
