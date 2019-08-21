# Manipulando arquivo txt

texto = "Cientista de Dados é a profissão que mais tem crescido em todo mundo.\n"
texto = texto + "Esses profissionais precisam se especializar em Programação, Estatística e Machine Learning.\n"
texto += "E claro, em Big Data."

# Pacote para manipular o Sistema Operacional
import os 

arquivo = open(os.path.join('arquivos/cientista.txt'), 'w')

for palavra in texto.split():
    arquivo.write(palavra+' ')

arquivo.close()

arq = open('arquivos/cientista.txt', 'r')
conteudo = arq.read()
arq.close()
# print(conteudo)

# Utilizando Whit

with open('arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()
# print(len(conteudo))
# print(conteudo)

# Utilizando slicing acessando grupos de caracteres

with open('arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:21])
    arquivo.write('\n')
    arquivo.write(texto[:33])

arq2 = open('arquivos/cientista.txt', 'r')
print(arq2.read())
arq2.close()