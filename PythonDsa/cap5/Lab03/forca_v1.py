# Lab03, exercicio de desenvolimento de uma forca utilizando python POO
import random

# tabuleiro
board = [
'''
 -----
 |   |
     |
     |
     |
     |
=========   
''',
'''
 -----
 |   |
 o   |
     |
     |
     |
=========   
''',
'''
 -----
 |   |
 o   |
 |   |
     |
     |
=========   
''',
'''
 -----
 |   |
 o   |
/|\  |
     |
     |
=========   
''',
'''
 -----
 |   |
 o   |
/|\  |
/ \  |
     |
=========
GAME OVER !   
'''
]


class Handgman():
    # Inicia a clase construtora
    def __init__(self, word):
        self.word = word
        print('Start Game !')

    # Metodo para adivinhar a letra    
    def guess(self, letter):
        if letter in self.word:
            return True
        else:
            return False

    # Metodo para verificar se o jogo terminou    
    def hangman_over(self):    
        pass

    # Metodo para verificar se o jogador venceu    
    def hangman_won(self):
        pass

    # Metodo para não motrar a palavra no board    
    def hide_word(self):
        print(self.word)
        secret = []
        for x in self.word:
            secret.append('_')
        return print('palavra %s'%(''.join(secret)))

    # Metodo para imprimir status do game    
    def print_status(self):
        pass

# Funcao para pegar palavra aleatoria do arquivo
def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)) -1 ].strip()



# Testes
game = Handgman(rand_word()) 
game.hide_word()

request = input('Entre com uma letra: ')

print(game.guess(request))
