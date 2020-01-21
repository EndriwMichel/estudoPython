# Utilizando pandas DataFrame para ler arquivos csv
import pandas as pd
import sys
import numpy as np

# Lendo o arquivo diretamente do repositorio
print('Lendo arquivo csv com pandas')
df_salarios = pd.read_csv('https://raw.githubusercontent.com/dsacademybr/PythonFundamentos/master/Cap08/Notebooks/salarios.csv')
print(df_salarios)
print('')

# Mudando as colunas do arquio csv
# Obs:. Porem a primeira linha que seria o cabeçalho torna-se uma linha de dado comun
print('Mudando as colunas do arquio csv')
df = pd.read_csv('https://raw.githubusercontent.com/dsacademybr/PythonFundamentos/master/Cap08/Notebooks/salarios.csv', 
                names=['a, b, c, d'])
print(df)
print('')

# Salvando arquivo csv apos trabalho de analise
# print('Salvando arquivo csv apos trabalho de analise')
data = pd.read_csv('https://raw.githubusercontent.com/dsacademybr/PythonFundamentos/master/Cap08/Notebooks/salarios.csv')
# data.to_csv(sys.stdout, sep='|')
print('')

# Criando um DataFrame com um range de datas
print('Criando um DataFrame com um range de datas')
dates = pd.date_range('20180101', periods=10)
print('Objeto dates')
print(dates)
print('')
print('DataFrame criando com numeros aleatorios e index de data')
df_dates = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list('ABCD'))
print(df_dates)
print('')

# Calculo de media
print('Calculo e media com mean (para todas as colunas)')
print(df_dates.mean())
print('')
print('Calculo e media com mean (pivot)')
print('Obs:. Calculando com base na data, o pibot é muito utilizando para calculos aonde agrupamos por outro tipo de informação, coluna ou linha')
print(df_dates.mean(1))
print('')

# Usando metodos
# Uilizando apply chamamos uma funação criada ou nativa de outro pacote para aplicar ao dataframe
print('Usando metodos')
print(df_dates.apply(np.cumsum))
print('')

# Merge de dataframes
print('Merge de DataFrames')
df_left = pd.DataFrame({'chave':['chave1', 'chave2'], 'coluna1':[1, 2]})
df_right = pd.DataFrame({'chave':['chave1', 'chave2'], 'coluna2':[4, 5]})
print(pd.merge(df_left, df_right, on='chave'))
print('')

# Adicionar elemento ao DataFrame
print('Adicionando elementos ao DataFrame')
df_elem = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df_elem)
print('')

s = df_elem.iloc[3]
print(s)
print('')
# Elemento adicionado
print(df_elem.append(s, ignore_index=True))
print('')
