# trabalhando com Pandas - Series e Dataframe
import pandas as pd

print(pd.__version__)

# Criando uma Serie
Obj = pd.Series([67, 78, -56, 13])
print(Obj)
print('')
print(Obj.values)

# Não ira trazer o index e sim a instrução
print(Obj.index)
print('')

# Criando serie com indexes epecificados
Obj2 = pd.Series([67, 78, -56, 13], index=['a', 'b', 'c', 'd'])
print(Obj2)
print('')

# Trazer valores com opções aritmeticas
print('Trazer tudo maior do que 3')
print(Obj2[Obj2 > 3])
print('')

# Fazer consultas
print('Efetuar consultas')
print('b' in Obj2)
print('')

# Criando series de dados com base em um dict

print('Criando series de dados com base em um dict')
dicti = {'Futebol':5200, 'Tenis':120, 'Natação':689, 'Volleyball':1550}
Obj3 = pd.Series(dicti)

print(Obj3)
print('')

# Criando series e setando os indexes
print('Criando series e setando os indexes')
esportes = ['Futebol', 'Tenis', 'Natação', 'Basketboll']

Obj4 = pd.Series(dicti, index=esportes)
print(Obj4)
print('')

# isnull e notnull
print('-- isnull --')
print(pd.isnull(Obj4))
print('')

print('-- notnull --')
print(pd.notnull(Obj4))
print('')

# Concatenamento de Series
# O python irá buscar relação entre os index das series e no que ele não encontrar, irá colocar valor nulo
print('Concatenamento de Series')
print(Obj3 + Obj4)
print('')

# Dar um nome para a Serie
print('Dar um nome para a Serie')
Obj4.name = 'população' 
Obj4.index.name = 'esporte' 
print('')

print(Obj4)