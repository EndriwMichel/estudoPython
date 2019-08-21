# Manipulando arquivo csv

import csv

# with open('arquivos/numeros.csv', 'w') as arquivo:
#     writer = csv.writer(arquivo)
#     writer.writerow(('primeira', 'segunda', 'terceira'))
#     writer.writerow((55, 93, 76))
#     writer.writerow((62, 14, 86))

with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for x in leitor:
        print('Numero de colunas', len(x))
        print(x)

print('')
# Convertendo em lista

with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    lista_csv = list(leitor)

print(lista_csv)

print('')
# Imprimindo a partir da posição 2

for i in lista_csv[1:]:
    print(i)

