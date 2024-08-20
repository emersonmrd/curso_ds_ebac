import requests
from bs4 import BeautifulSoup
import pandas as pd

# Site : https://br.financas.yahoo.com/quote/%5EBVSP/history/?guccounter=1

url = "https://br.financas.yahoo.com/quote/%5EBVSP/history/?guccounter=1"

print("REQUEST: ")
response = requests.get(url)
print(response.text[:600])

print("SOUP: ")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify()[:1000])

print("PANDAS: ")
url_dados = pd.read_html(url)
print(url_dados[0].head())