# Função map
# Função utilizada para executar diversas vezes uma outra função com varios valores, por exemplo uma lista 

def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celcius(T):
    return (float(5)/9)*(T - 32)

temperaturas = [0, 22.5, 40, 100]

print(map(fahrenheit, temperaturas))

print(list(map(fahrenheit, temperaturas)))

print('')

for temp in map(fahrenheit, temperaturas):
    print(temp)

print('')

print(list(map(celcius, temperaturas)))

print(list(map(lambda x: (5/9) * (x - 32), temperaturas)))

# Somando elementos entre listas
print('')
print('Somando 2 listas')
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(list(map(lambda x, y: x+y, a, b)))

print('')
print('Somando 3 listas')
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

print(list(map(lambda x, y, z: x+y+z, a, b, c)))