import math

def is_prime(N):
    if N < 2:
        return False
    for i in range(2,math.isqrt(N) + 1):
        if N%i == 0:
            return False
    return True

def get_factores(number):
    divisors = []
    for i in range(2,math.isqrt(number) + 1):
        while number % i == 0:
            number = number // i
            if i not in divisors:
                divisors.append(i)
            if number not in divisors and i!=number:
                divisors.append(number)
    return divisors

def get_factores_primes(divisors):
    factores_primes = []
    for divisor in divisors:
        if is_prime(divisor):
            factores_primes.append(divisor)
    return factores_primes

def main(number):
    
    ## Calculando todos los divisores
    divisors = get_factores(number)
    
    ## Calculando todos los divisores primos
    factores_primes = get_factores_primes(divisors)

    prime_large = max(factores_primes)

    print("El factor primo mas grande del número {} es:{}".format(number,prime_large))

main(600851475143)