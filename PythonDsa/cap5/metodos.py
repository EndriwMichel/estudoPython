# Metodos 

class Circulo():

    pi = 3.14
    # Definindo o objeto da classe com o valor default de 5, caso não seja entrado um valor será usado esse
    def __init__(self, raio = 5):
        self.raio = raio

    def area(self):
        return (self.raio * self.raio) * Circulo.pi

    def setRaio(self, novo_raio):
        self.raio = novo_raio

    def getRaio(self):
        return self.raio

circ = Circulo()

print('O raio é :', circ.getRaio())
print('A area é :', circ.area())

print('--- Alterando o valor ---')
circ.setRaio(3)
print('O novo valor de raio é :', circ.getRaio())
print('O novo valor da area é :', circ.area())