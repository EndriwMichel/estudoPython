# funcao enumerate
# enumerte retorna os indices de uma lista de valores

seq = ['a', 'b', 'c']

print(list(enumerate(seq)))

for k, v in enumerate(seq):
    print(k, v)

# Exemplo com string
print('')
for i, string in enumerate('isso é uma string'):
    print(i, string)