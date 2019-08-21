# Trabalhando com arquivos
print('')

arq = open('arquivos/arquivo1.txt', 'r')
print('read')
print(arq.read())
print('')
print('tell')
print(arq.tell())
print('')
print('seek')
print(arq.seek(0, 0))
print('')
print('read 10')
print(arq.read(10))
print('')

# Abrir o arquivo para escrita "sobrescrever"

arq2 = open('arquivos/arquivo1.txt', 'w')
arq2.write('Tetando gravação em arquivos Python')
arq2.close()

# Abrir o arquivo para escrita "append", acrescentar
arq2 = open('arquivos/arquivo1.txt', 'a')
arq2.write(' Acrescentando conteúdo')
arq2.close()

# Outro Exemplo

# name = input('entre com o nome do arquivo: ')

# filename = name + '.txt'

# arq3= open(filename, 'w')
# arq3.write('Informação no arquivo')

# arq3.close()

arq3 = open('arquivos/arquivo1.txt', 'r')

print(arq3.read())
arq3.seek(0)
print(arq3.readlines())

arq3.close()

# Utilizando for

arq3 = open('arquivos/arquivo1.txt', 'r')

for line in arq3:
    print(line)

