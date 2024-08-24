import pandas as pd

df = pd.read_csv("./coleta_dados/clientes.csv")

# Verificar os primeiros registros
print(df.head().to_string())

# Verificar os últimos registros
print(df.tail().to_string())

# Verificar qtd de linhas e colunas
print("Qtd: ", df.shape)

# verificar tipos de dados
print("Tipagem:\n", df.dtypes)

# Checar valores nulos
print("alores nulos:\n", df.isnull().sum())