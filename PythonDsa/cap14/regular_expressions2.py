# Expressoes regulares continuação
import re

def encontra_padrao(lista, frase):

    for item in lista:
        print('Pesquisando na frase %r' %item)
        print(re.findall(item, frase))
        print('\n')

frase_padrao = 'zLzL..zzzLLL...zLLLzLLL...LzLz...dzzzzz...zLLLL'

lista_padroes = [ 'zL*',       # z seguido de zero ou mais L
                  'zL+',       # z seguido por um ou mais L
                  'zL?',       # z seguido por zero ou um L
                  'zL{3}',     # z seguido por três L
                  'zL{2,3}',   # z seguido por dois a três L
                ]

# encontra_padrao(lista=lista_padroes, frase=frase_padrao)


frase = 'Esta é uma string com pontuação. Isso pode ser um problema quando fazemos mineração de dados em busca '\
        'de padrões! Não seria melhor retirar os sinais ao fim de cada frase?'

# print(re.findall('[^!.?]+', frase))        

frase = 'Esta é uma frase de exemplo. Vamos verificar quais padrões serão encontrados.'

lista_padroes = [ '[a-z]+',      # sequência de letras minúsculas
                  '[A-Z]+',      # sequência de letras maiúsculas
                  '[a-zA-Z]+',   # sequência de letras minúsculas e maiúsculas
                  '[A-Z][a-z]+'] # uma letra maiúscula, seguida de uma letra minúscula

# encontra_padrao(lista_padroes, frase)

# Escape Codes

# O prefixo r antes da expressão regular evita o pré-processamento da ER 
# pela linguagem. Colocamos o modificador r (do inglês "raw", crú) 
# imediatamente antes das aspas
print(r'\b')

frase = 'Esta é uma string com alguns números, como 1287 e um símbolo #hashtag'

lista_padroes = [ r'\d+', # sequência de dígitos
                  r'\D+', # sequência de não-dígitos
                  r'\s+', # sequência de espaços
                  r'\S+', # sequência de não-espaços
                  r'\w+', # caracteres alfanuméricos
                  r'\W+', # não-alfanumérico
                ]

encontra_padrao(lista_padroes, frase)