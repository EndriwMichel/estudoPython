# Orientação a objetos, classes
class livro():
    # __init__ é utilizado parainicializar cada objeto da classe
    def __init__(self):
        # Self significa que são atributos dos objetos
        self.titulo = 'O Monge e o Executivo'
        self.isbn = 9988888
        print('Construtor chamado para criar um objeto desta classe')
    
    def imprime(self):
        return print('Foi criado o livro %s e o isbn %d' %(self.titulo, self.isbn))

livro1 = livro()

print(type(livro1))
print(livro1.imprime())

