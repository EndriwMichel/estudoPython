# Convertendo páginas web para pandas
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

res = requests.get('http://www.nationmaster.com/country-info/stats/Media/Internet-users')

soup = BeautifulSoup(res.content, 'lxml')

table = soup.find_all('table')[0]

# Convertendo para pandas
df = pd.read_html(str(table))
print(df)

# Conversão do pandas para um objeto Json
print(df[0].to_json(orient='records'))

# Utilizando o tabulate para formatar a saida da informação
print(tabulate(df[0], headers='keys', tablefmt='psql'))