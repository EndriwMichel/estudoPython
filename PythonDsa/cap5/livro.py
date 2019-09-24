# Nova classe livro
class livro():
    def __init__(self, titulo, isbn):
        # Self é uma referencia de cada atributo de um objeto criado a partir desta classe
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto desta classe')
    
    def imprime(self, titulo, isbn):
        return print('Foi criado o livro %s e o isbn %d' %(titulo, isbn))

livro2 = livro('A menina que roubava', 989898)

# print(livro2.titulo)

livro2.imprime('A menina que roubava', 989898)


class cachorro():
    def __init__(self, raça):
        self.raça = raça
        print('Construtor chamado para criar um objeto desta classe')

Rex = cachorro(raça = 'labrador')
Golias = cachorro(raça = 'Huskie')

print(Rex.raça)
print(Golias.raça)