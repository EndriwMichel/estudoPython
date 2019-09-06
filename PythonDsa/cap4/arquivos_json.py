# Manipulando Json
import json
from urllib.request import urlopen
import os

dic = {'nome': 'Guido Van Rossum',
       'linguagem': 'Python',
       'similar': ['c', 'modula-3', 'lisp'],
       'users': 10000000}

for k,v in dic.items():
    print(k, v)     


print(json.dumps(dic))


with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dic)) 

with open('arquivos/dados.json', 'r') as arquivo:
    data = json.loads(arquivo.read())
    print(data['nome'])    

# Efetuando requisição em url
print('')
response = urlopen('http://vimeo.com/api/v2/video/57733101.json').read().decode('utf8')
data = json.loads(response)[0]

print('titulo: ', data['title'])
print('URL: ', data['url'])
print('Duração: ', data['duration'])
print('Número de Visualizações: ', data['stats_number_of_plays'])

# Copiando conteudo para outro arquivo

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

with open(arquivo_fonte, 'r') as arquivo_f:
    text = arquivo_f.read()
    with open(arquivo_destino, 'w') as arquivo_d:
        arquivo_d.write(text)

# Metodo 2
open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

# Leitura de arquivos Json

with open('arquivos/json_data.txt') as arquivo:
    texto = arquivo.read()
    data = json.loads(texto)
    print(data)
    