import requests
from bs4 import BeautifulSoup

url = "https://wiki.python.org.br/AprendaMais"
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, "html.parser")

# Exibir o texto
# print(extracao.text.strip())

# contador de titulos e paragrafos
cont_titulo = 0
cont_paragrafo = 0

# Filtrar a exibição pela tag
# for linha_texto in extracao.find_all(['h2', 'p']):
#     titulo = linha_texto.text.strip()
#     if linha_texto.name == 'h2':
#         cont_titulo += 1
#     if linha_texto.name == 'p':
#         cont_paragrafo += 1
#     print("Titulo: ", titulo)
# print(f"O total de títulos é {cont_titulo} e o total de parágrafos é {cont_paragrafo}")

# Exibir somente o texto das tag h2 e p
# for linha_texto in extracao.find_all(['h2', 'p']):
#     if linha_texto.name == 'h2':
#         titulo = linha_texto.text.strip()
#         print(f"Título: \n{titulo}")
#     elif linha_texto.name == 'p':
#         paragrafo = linha_texto.text.strip()
#         print(f"Paragrafo: \n{paragrafo}")

# Exibir tagas Aninhada
for titulo in extracao.find_all('h2'):
    print(f"\n Titulo: {titulo.text.strip()}")
    for link in titulo.find_next_siblings("p"):
        for a in link.find_all("a", href=True):
            print(f"Texto Link: {a.text.strip()} | URL:{a['href']}")
