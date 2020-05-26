# Expressões regulares
import re

lista_pesquisa = ['informações', 'Negócios']

texto = 'Existem muitos desafios para o Big Data. O primeiro deles é a coleta dos dados, pois fala-se aqui de '\
'enormes quantidades sendo geradas em uma taxa maior do que um servidor comum seria capaz de processar e armazenar. '\
'O segundo desafio é justamente o de processar essas informações. Com elas então distribuídas, a aplicação deve ser '\
'capaz de consumir partes das informações e gerar pequenas quantidades de dados processados, que serão calculados em '\
'conjunto depois para criar o resultado final. Outro desafio é a exibição dos resultados, de forma que as informações '\
'estejam disponíveis de forma clara para os tomadores de decisão.'

# Exemplo simples dedata mining

for item in lista_pesquisa:
    print('Busca por %s em \n\n"%s"' % (item, texto))

    # Verificando existencia do termo
    if re.search(item, texto):
        print('\n')
        print('Palavra encontrada!\n')
        print('\n')
    else:
        print('\n')
        print('Palavra não encontrada!\n')
        print('\n')

# Dividir uma string
split_term = '@'

frase = 'Qual o domínio de alguém com o e-mail: aluno@gmail.com'

# Dividindo a frase
print(re.split(split_term, frase))
