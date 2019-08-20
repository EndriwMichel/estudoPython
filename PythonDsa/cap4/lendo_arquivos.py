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
arq2.write('Acrescentando conteúdo')
arq2.close()
