from itertools import permutations
import math

def isPrime(N):
    if N < 2:
        return False
    for i in range(2,math.isqrt(N) + 1):
        if N%i == 0:
            return False
    return True

def main(N):
    val_max = 0
    seq_primes = []
    for i in range(2,N+1):
        numeros = list(range(1,i + 1))
        permutaciones = permutations(numeros)
        numeros_generados = [''.join(map(str, perm)) for perm in permutaciones]
        numeros_generados = list(map(int, numeros_generados))
        numeros_generados = sorted(numeros_generados)
        cnt_numeros_generador = len(numeros_generados)
        for numero in numeros_generados:
            if isPrime(numero) and cnt_numeros_generador:
                if numero>val_max:
                    val_max = numero
                    seq_primes.append(numero)
    
    return max(seq_primes)


also_prime = main(9)
print(also_prime)