# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e 
# depois faça uma chamada à função para listar os números011
def imprimeNumeros():
    for i in range(0, 21, 2):
        print(i) 

imprimeNumeros()

# Exercício 2 - Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas.
# Faça uma chamada à função, passando como parâmetro uma string

def retornaMaiusculo(valor):
        return print(valor.upper())

retornaMaiusculo('string')

# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista

def recebeElementos(*lista):
        lista_convert = list(lista)
        for i in range(1, 3):
                lista_convert.append('valorAdicional%d'%(i))
        return print(lista_convert)

recebeElementos('valor1', 'valor2', 'valor3', 'valor4')

# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
# à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def elementoFormal(arg1, *argList):
        print(arg1)
        for i in argList:
                print(i)
        return

elementoFormal('valor')
# print('')
elementoFormal('valor1', 'valor2', 'valor3', 'valor4')


# Exercício 5 - Crie uma função anônima e atribua seu retorno a uma variável chamada soma. A expressão vai receber 2 
# números como parâmetro e retornar a soma deles

soma = lambda x,y: x+y
print(soma(5, 7))

# Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local
total = 0 #variavel criada fora da função, variavel global
def soma( arg1, arg2 ):
    total = arg1 + arg2; #variavel criada dentro da função, variavel local
    print ("Dentro da função o total é: ", total)
    return total;


soma( 10, 20 );
print ("Fora da função o total é: ", total)

# Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
# Crie uma função anônima que converta cada temperatura para Fahrenheit
# Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
# (que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista
# Como descobrir a fórmula matemática que converte de Celsius para Fahrenheit? Pesquise!!!
# Celsius = [39.2, 36.5, 37.3, 37.8]
# Fahrenheit = map(coloque_aqui_sua_função_lambda)
# print (list(Fahrenheit))
Celsius = [39.2, 36.5, 37.3, 37.8]

celToFah = lambda x: (x * 9/5) + 32

Fahrenheit = map(celToFah, Celsius)
print (list(Fahrenheit))

# Exercício 8
# Crie um dicionário e liste todos os métodos e atributos do dicionário

dic = {'key1':'value1', 'key2':'value2'}
print(dir(dic))

# Exercício 9
# Abaixo você encontra a importação do Pandas, um dos principais pacotes Python para análise de dados.
# Analise atentamente todos os métodos disponíveis. Um deles você vai usar no próximo exercício.
import pandas as pd
# print(dir(pd))


# ************* Desafio ************* (pesquise na documentação Python)

# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo 
# do arquivo. Dica, use Pandas e um de seus métodos, describe()
# Arquivo: "binary.csv"
# import pandas as pd

data = ('C:/Users/Endriw/Documents/Py/estudoPython/PythonDsa/cap3/binary.csv') 

def descreveCsv(file):
        csv = pd.read_csv(file)
        return csv.describe()

print(descreveCsv(data))
#imprime uma descrição em relação ao percetual das informações e médias 
