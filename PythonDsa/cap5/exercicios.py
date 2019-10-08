# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada
# aos atributos e métodos
from math import sqrt

class Rocket():
     
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_rocket(self, x_increment=0, y_increment=1):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)


roc1 = Rocket(3, 5)
roc1.print_rocket()
roc1.move_rocket(3, 5)
roc1.print_rocket()


# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.


class Pessoa():
    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return '%s mora na cidade: %s, possui o telefone: %s e o respectivo email: %s' %(self.nome, self.cidade, self.telefone, self.email)

    def __hash__(self):
        return hash((self.nome, self.cidade, self.telefone, self.email))

pessoa1 = Pessoa('Jão', 'Sumaré', '19-98888-3535', 'jão@gmail.com')

print(pessoa1)

print(hash(str(pessoa1)))