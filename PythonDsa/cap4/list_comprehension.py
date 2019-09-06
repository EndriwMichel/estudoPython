# Função List Comprehension

lst = [x for x in 'Python']

print(lst)

lst = [x**2 for x in range(1, 11)]

print(lst)

# Complicando um pouco a list comprehension

lst = [x for x in range(11) if x % 2 == 0]

print(lst)

celcius = [0, 10, 20.1, 34.5]

fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celcius ]

print(fahrenheit)

lista = [x**2 for x  in [x**2 for x in range(11)]]

print(lista)