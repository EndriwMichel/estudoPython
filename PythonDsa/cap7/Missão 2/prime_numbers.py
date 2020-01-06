# Gerar uma lista de numeros primos
import math


class PrimeGenerator(object):

    def generate_primes(self, max_num):
        matrix = [x for x in range(2, max_num+1)]
        return matrix       

    def _cross_off(self, array):
        aux_arr = []
        prime_arr = []
        for x in array:
#            if x != 2:
            for y in range(2, x):
                if x % y == 0:
                    aux_arr.append(True)
                else:
                    aux_arr.append(False)
            if True not in aux_arr:     
                prime_arr.append(True)
                del aux_arr[:]
            else:
                prime_arr.append(False)
                del aux_arr[:]

        return prime_arr

    def _next_prime(self, array, primes):
        print_primes = []
        for x, y in zip(array, primes):
            if y == True:
                print_primes.append(x)

        return print(print_primes)


valor = PrimeGenerator()

max_number = input('Entre com um numero maximo para saber seus primos: ')

ranged_primes = valor.generate_primes(int(max_number))

primes = valor._cross_off(ranged_primes)

valor._next_prime(ranged_primes, primes)