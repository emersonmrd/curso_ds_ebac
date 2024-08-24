import pandas as pd

df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Escreva seu código abaixo

# Extrair e limpar os dados da coluna 'Condicao'
# A função lambda é usada aqui para pegar a primeira palavra da string na coluna 'Condicao'
# x.split(' ')[0] pega a primeira palavra da string.
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split('|')[0].strip())

# A função lambda é usada aqui para pegar a quinta palavra da string na coluna 'Condicao' se existir,
# caso contrário, retorna 'Nenhum'
df['Qtd_Vendidos'] = df['Condicao'].apply(lambda x: x.split('|')[1].strip().split(" ")[0] if len(x.split('|')) > 1 else 'Nenhum')
print(df.head())

# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

# A função lambda é usada aqui para remover o símbolo '%' da string na coluna 'Desconto'
df['Desconto'] = df['Desconto'].apply(lambda x: x.split('%')[0].strip())
