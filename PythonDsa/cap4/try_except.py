# Try e Except
# Try e Except são utilizados para tratar excessoes, excessoes são erros retornados não esperados, diferente de erros de sintaxe

def numDiv(num1, num2):
    resultado = num1/num2
    return resultado

try:
    print(numDiv(4, 0))
except:
    print('erro')

# Except de tipo
print('')

try:
    8 + 's'
except TypeError:
    print('Operação invalida')

# Except de IO, para arquivos
try:
    f = open('arquivos/testandoerros.txt', 'w')
    f.write('Gravando no arquivo')
except IOError:
    print('Arquivo nao pode ser aberto !')
else:
    print('Conteudo gravado com sucesso !')
    f.close

print('')

try:
    f = open('arquivos/testandoerros', 'r')
except IOError:
    print('Arquivo nao pode ser aberto !')
else:
    print('Conteudo gravado com sucesso !')
    f.close

print('')
# Finally sempre será executado independente do resultado
try:
    f = open('arquivos/testandoerros', 'r')
except IOError:
    print('Arquivo nao pode ser aberto !')
else:
    print('Conteudo gravado com sucesso !')
    f.close
finally:
    print('Sempre será executado !')

# Exemplo com uma funcao

def askInt():
    while True:
        try:
            val = int(input('Digite um numero: '))
        except:
            print('Você não digitou um numero !')
            continue
        else:
            print('Digitou um numero !')
            break    
        finally:
            print('Encerrado...')
        print(val)

# descomentar para ver o exemplo acima
# askInt()

# Caputando codigo de erro

tup = (1, 2, 3, 4, 5)

try:
    tup.append(6)
    for i in tup:
        print(i)
except AttributeError as e:
    print('Erro de atributo: ', e)
except IOError as e:
    print('Erro de IO: ', e)
    