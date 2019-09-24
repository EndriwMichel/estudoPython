# Objetos

#Type é utilizado para verificar o tipo dos objetos

print(type(10))
print(type([]))
print(type(()))
print(type({}))
print(type('a'))

class carro():
    pass

palio = carro()

print(type(palio))

class estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

Estudante1 = estudantes('Pele', 12, 5.5)
print(Estudante1.nome)
print(Estudante1.idade)
print(Estudante1.nota)

class funcionarios:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def list_func(self):
        print('O nome do funcionario é '+self.nome+' e seu salario é R$'+str(self.salario))

Func1 = funcionarios('Obama', 2000)

Func1.list_func()

print('*** Usando atributos ***')
 
print(hasattr(Func1, 'nome'))
print(hasattr(Func1, 'salario'))
print(setattr(Func1, 'salario', 4500))
print(hasattr(Func1, 'salario'))
print(getattr(Func1, 'salario'))
print(delattr(Func1, 'salario'))
print(hasattr(Func1, 'salario'))
