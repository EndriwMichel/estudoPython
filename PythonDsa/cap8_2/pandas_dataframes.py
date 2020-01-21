# Pandas Dataframes
from pandas import DataFrame
import numpy as np

# Cria a lista de valores
data = {
    'Estado':['Santa Catarina', 'Goais', 'Parana', 'Bahia', 'Minas Gerais'],
    'Ano':[2002, 2003, 2004, 2005, 2006],
    'População':[1.5, 1.7, 3.6, 2.4, 2.9]
}

# Gera Dataframe com a lista
frame = DataFrame(data)
print('Exemplo de Dataframe')
print(frame)
print('')

# Reorganizando e acessando as colunas
print('Reorganizando e acessando as colunas')
frame = DataFrame(data, columns=['Ano', 'Estado', 'População'])
print(frame)
print('')

# Adicionando novas colunas e criando index
print('Adicionando novas colunas e criando index')
frame2 = DataFrame(data, columns=['Ano', 'Estado', 'População', 'Débito'], index=['um', 'dois', 'tres', 'quatro', 'cinco'])
print(frame2)
print('')

# Operações
print('---- Indices ----')
print(frame2.index)
print('')
print('---- Colunas ----')
print(frame2.columns)
print('')
print('---- Valores ----')
print(frame2.values)
print('')
print('---- Tipos ----')
print(frame2.dtypes)
print('')

# Buscar informações de uma coluna
# OBs.: Duas formas frame2['Ano'] ou frame2.Ano
print('Buscar informações de uma coluna')
print(frame2.Ano)
print('')

# Slicing em Dataframe
print('Slicing de Dataframe')
print(frame2[:2])
print('')

# Preenchendo os valores null (NaN) da coluna débito
print('Preenchendo os valores null (NaN) da coluna débito')
frame2['Débito'] = np.arange(5.) 
print(frame2)
print('')
print('Verificando os valores em formato de array')
print(frame2.values)
print('')

# método describle para retornar estatisticas sobre o dataframe
print('Resumo estatistico sobre DataFrame')
print(frame2.describe())
print('')

# Slicing em DataFrame
print('Slicing em DataFrame')
print(frame2['dois':'quatro'])
print('')

# Localizando registros dentro do DataFrame
print('Localizando registros dentro do DataFrame')
print(frame2.loc['quatro'])
print('')
print('Busca pelo index')
print(frame2.iloc[2])
print('')

# Invertendo colunas em indices
print('Invertendo colunas em indices')
web_stats = {'Dias':[1, 2, 3, 4, 5, 6, 7],
            'Visitantes':[45, 23, 67, 68, 23, 12, 14],
            'Taxas':[11, 22, 33, 44, 55, 66, 77]}

df_web = DataFrame(web_stats)

print(df_web)
print('')

print('Transformando a coluna Dias em um index')
print(df_web.set_index('Dias'))
print(df_web.head)
print('')
print(df_web['Visitantes'])