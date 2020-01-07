# Pandas Dataframes
from pandas import DataFrame

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