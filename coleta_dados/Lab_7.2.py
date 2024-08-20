import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0

for linha_texto in extracao.find_all("article", class_="product_pod"):
    for titulo in linha_texto.find_all("h3") :
        if titulo.name == "h3":
            texto_titulo = titulo.text.strip()
            contar_livros += 1
            print('\nTítulo:', texto_titulo)
        for preco in linha_texto.find_all("p", class_="price_color"):
            preco_texto = preco.text.strip()
            print('Preço:', preco_texto)

print('Total livros:', contar_livros)
