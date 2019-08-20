# Calculadora em Python

# imprimir cabeçalho de "front"
print('=========Python Ultra Calculator 2000=========')
print('')
print('Selecione a operação que deseja efetuar: ')
print('')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('')

#  Função responsavel por efetuar os calculos
def efetuaCalculos(opc, val1, val2):
    result = 0 
    sign = ''
    # Calcula Soma
    if opc == 1:
        result = val1 + val2
        sign = ' + '
    # Calcula Subtração    
    elif opc == 2:
        result = val1 - val2
        sign = ' - '
    # Calcula Multiplicação
    elif opc == 3:
        result = val1 * val2
        sign = ' * '
    # Calcula Divisão
    elif opc == 4:
        result = val1 / val2
        sign = ' / '
    # Retorna valor final com os valores que foram digitados
    final_result = str(val1)+sign+str(val2)+' = '+str(result)
    return print(final_result)        


# Solicita ao usuario uma opção
opcao = input('Digite sua opção 1/2/3/4: ')

try:
    # Se opção for diferente das possiveis, imprime erro na tela
    if int(opcao) not in [1, 2, 3, 4]:
        print('')
        print('Opção Inexistente !')
        print('')
    # Se não, pede ao usuario os numeros para efetuar calculo
    else:
        valor1 = input('Digite o primeiro número: ')
        valor2 = input('Digite o segundo número: ')
        print('')

        efetuaCalculos(int(opcao), int(valor1), int(valor2))
except:
    # Retorna menssagem de erro caso usuario digite algo que não seja um número
    print('')
    print('Por favor digite apenas numeros !')
