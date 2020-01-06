# Desafio 1
# Verificar se uma palavra possui todos os caracteres especiais
import re

class VerifyString():
# Classe para verificar caracteres especiais em uma string
    def __init__(self, v_string):
        self.v_string = v_string
        print('Iniciando analise da string')
        print('...')

    def slice_string(self):
        # Fatia a string e retorna caracteres em um array
        slicing_string = [x for x in self.v_string]
        return slicing_string

    def verify_letters(self, slicing_string):
        # Verifica por caracteres especiais e retorna um objeto com dois arrys contendo caracteres especiais e verdadeiro ou falso 
        characters = []
        special_chars = []

        for x in slicing_string:
            if re.match('^[a-zA-Z0-9_]*$', x):
                characters.append(True)
            else:
                characters.append(False)
                special_chars.append(x)
        return {'characters': characters, 'special_chars': special_chars}

    def verify_special(self, slice_string, special_chars):
        # Valida se a palavra possui somente ou nenhum e quais são os caracteres especiais
        if True not in slice_string:
            return print('A palavra SOMENTE possui caracteres especiais !')
        elif False not in slice_string:
            return print('A palavra não possui caracteres especiais !')
        else:
            return print('A palavra possui caracteres especiais: %s'%(special_chars))

# Solicita palavra para o usuario
entered_word = input('Entre com uma palavra: ')

# Inicia classe
word = VerifyString(entered_word)

# Fatia string por caracter
sliced_string = word.slice_string()

# Retorna objeto com analise
object_word = word.verify_letters(sliced_string)

# Valida se a palavra possui ou não e quantos caracteres especiais
word.verify_special(object_word['characters'], object_word['special_chars'])