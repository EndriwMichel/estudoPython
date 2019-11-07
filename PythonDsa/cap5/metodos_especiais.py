# Metodos Especiais

class Livro():
    def __init__(self, titulo, autor, paginas):
        print('livro criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return 'Titulo: %s, autor: %s, paginas: %s ' %(self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas

    def len(self):
        return print('Paginas do livro com metodo comum: ', self.paginas)

livro1 = Livro('Os Lusiadas', 'Luis Camaroes', 8816)

# Sempre que chamar um print automaticamente o python ira chamar o metodo __str__ por isso imprime a menssagem
print(livro1)

str(livro1)

# Quando chamar o metodo len ele tbm ira trazer automaticamente o que foi definido no __len__ no metodo da classe 
print(len(livro1))

print(livro1.len())

# Deletando as paginas utilizando metodo especial del que deleta automaticamente a informação de um metodod ja instanciado
print('--- Deletando as paginas ---')
del livro1.paginas
#livro1.__delattr__('paginas')

print(hasattr(livro1, 'paginas'))
print(hasattr(livro1, '__len__'))
