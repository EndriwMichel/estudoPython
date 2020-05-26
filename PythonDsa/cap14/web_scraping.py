# Web Scraping
# Obs.: No curso é utilizado a lib urllib.request porém optei para utilizar o requests que é uma versão renovada e muito melhor da lib
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.python.org/')

# print(page.content)

# Parse da informação
soup = BeautifulSoup(page.content, 'html.parser')

# Imprimindo o titulo da página
# print(soup.title.string) -- também funciona
print(soup.title.text)

print(soup.find_all('a'))

tables = soup.find('table')

print(tables)