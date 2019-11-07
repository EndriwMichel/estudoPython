# Trabalhando com csv

# f = open('arquivos\salarios.csv', 'r')
# data = f.read()

# rows = data.split('\n')

# print(rows[1])

# Outro exemplo

f = open('arquivos\salarios.csv', 'r')
data = f.read()

rows = data.split('\n')

full_data = []

for i in rows:
    split_row = i.split(',')
    full_data.append(split_row)

print(full_data[1][0])   

count = 0

for i in full_data:
    count += 1

print('Quantidade de linhas: '+str(count))

for i in rows:
    split_row = i.split(',')
    full_data.append(split_row)

first_row = full_data[0]
count_column = 0

for columns in first_row:
    count_column += 1

print('Quantidade de colunas: '+str(count_column))
