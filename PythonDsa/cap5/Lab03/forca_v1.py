# Lab03, exercicio de desenvolimento de uma forca utilizando python POO
import random 
import dicas

# Tabuleiro
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
/|   |
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
/    |
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

# Variaveis utilizadas ao decorrer do programa
guess_word = []
just_word = ''
correct_word = []
used_letters = []
arr_word = ''
error = 0
winner = False
looser = False

class Handgman():
    # Inicia a clase construtora
    def __init__(self, word):
        self.word = word
        print('====== Start Game ! ======')
        print('Dica: ')
        print('A palavra é um(a) %s e contém %i letras'%(dicas.devolve_dica(word), len(word)))

    # Metodo para adivinhar a letra    
    def guess(self, letter):
        if letter in self.word:
            return True
        else:
            return False

    # Metodo para verificar se o jogo terminou    
    def hangman_over(self, error):
        if error == len(board)-1:
            return True
        else:
            return False    
        pass

    # Metodo para verificar se o jogador venceu    
    def hangman_won(self, guess_word, correct_word):
        if ''.join(guess_word) == correct_word:
            return True
        else:
            return False
        pass

    # Metodo para não motrar a palavra no board    
    def hide_word(self):
        secret = []
        for x in self.word:
            secret.append('_')
        return secret #print('palavra %s'%(''.join(secret)))

    # Metodo para mostrar palavra no board
    def show_word(self, arr_word, correct_word, letter):
       list_index = [i for i, word in enumerate(correct_word) if word == letter]
       for i, word in enumerate(arr_word):
           if i in list_index:
               arr_word[i] = letter
       return ''.join(arr_word)

    # Metodo para imprimir status do game    
    def print_status(self, error, letters, arr_word):
        print(board[error])
        print('Letras que já foram: %s'%(letters))
        print('Palavra: %s'%(' '.join(arr_word)))

# Funcao para pegar palavra aleatoria do arquivo
def rand_word():
    with open('palavras.txt', 'rt') as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)) -1 ].strip()


# Utiliza a função para pegar uma palavra randomicamente
just_word = rand_word()

# Transforma a palavra em array para trabalhar com ela
correct_word = [x for x in just_word]


# Chama a Classe para iniciar o game
game = Handgman(just_word) 

# esconde a palavra e a transforma em um array 

guess_word = [x for x in game.hide_word()]

# Pede uma letrar para o usuario
while looser != True and winner != True:

    game.print_status(error, used_letters, guess_word)
    letter = input('Entre com uma letra: ')

    # Adiciona a letra ao array de letras utilizadas
    used_letters.append(letter)

    # Se caso a palavra conter a letra 
    if game.guess(letter) == True:
        arr_word = game.show_word(guess_word, correct_word, letter)
    else:
        error = error+1

    winner = game.hangman_won(arr_word, just_word)
    looser = game.hangman_over(error)        

if winner == True:
    game.print_status(error, used_letters, guess_word)
    print('-----------------------------------------------------------')
    print('Parabéns você acertou a palavra !')
    print(just_word)
    print('-----------------------------------------------------------')
if looser == True:
    game.print_status(error, used_letters, guess_word)
    print('-----------------------------------------------------------')
    print('Infelizmente você perdeu ! A palavra era: %s'%(just_word))
    print('-----------------------------------------------------------')


# End code