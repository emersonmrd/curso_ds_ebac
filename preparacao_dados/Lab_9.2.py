import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')

# Escreva seu código abaixo
print(df.head().to_string())
scaler = MinMaxScaler()
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])
scaler = MinMaxScaler()
df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])
scaler = MinMaxScaler()
df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])
scaler = MinMaxScaler()
df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])


label_encoder = LabelEncoder()
df['Marca_Cod'] = label_encoder.fit_transform(df['Marca'])
label_encoder = LabelEncoder()
df['Material_Cod'] = label_encoder.fit_transform(df['Material'])
label_encoder = LabelEncoder()
df['Temporada_Cod'] = label_encoder.fit_transform(df['Temporada'])