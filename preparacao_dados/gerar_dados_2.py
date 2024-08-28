import pandas as pd
import random
from faker import Faker

faker = Faker('pt_BR') # Seta os dados localizados para o Brasil

df = pd.read_csv('./tratamento_dados/clientes_tratados.csv')

print(df.head(10).to_string())

# Listas de opções para gerar valores aleatórios
niveis_educacao = ['Ensino Fundamental', 'Ensino Médio', 'Graduação', 'Pós-Graduação', 'Mestrado', 'Doutorado']
estados_civis = ['Solteiro(a)', 'Casado(a)', 'Divorciado(a)', 'Viúvo(a)']
areas_atuacao = ['TI', 'Educação', 'Saúde', 'Engenharia', 'Administração', 'Marketing']

# Gera valores aleatórios para todas as linhas do DataFrame
df['salario'] = [faker.random_int(min=1500, max=10000) for _ in range(len(df))]
df['nivel_educacao'] = [random.choice(niveis_educacao) for _ in range(len(df))]
df['numero_filhos'] = [faker.random_int(min=0, max=5) for _ in range(len(df))]
df['estado_civil'] = [random.choice(estados_civis) for _ in range(len(df))]
df['area_atuacao'] = [random.choice(areas_atuacao) for _ in range(len(df))]

# Exibe as primeiras linhas do DataFrame atualizado
print(df.head(10).to_string())

df.to_csv("clientes_tratados_v2.csv")

