# Herança

# Classe anima - "super classe"
class Animal():
    def __init__(self):
        print('Animal criado')

    def Identif(self):
        print('Animal')

    def comer(self):
        print('comendo')

# Classe cachorro - sub classe
class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Objeto cachorro criado')

    def Identif(self):
        print('Cachorro')

    def latir(self):
        print('Au au!')


# Definindo objeto 
rex = Cachorro()

print(rex.Identif())
print(rex.comer())
print(rex.latir())

#rex.Identif()