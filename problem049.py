import  math

def isPrime(N):
    if N < 2:
        return False
    for i in range(2,math.isqrt(N) + 1):
        if N%i == 0:
            return False
    return True

def son_permutaciones(num1, num2, num3):
    return (sorted(str(num1)) == sorted(str(num2)) and sorted(str(num2)) == sorted(str(num3)))

def get_primes(cota):
    numers_primes = []

    for number in range(cota):
        if(isPrime(number)):
            numers_primes.append(number)
    
    print("numers_primes:",numers_primes)

    return numers_primes

def main(primes):
    n = len(primes)
    for j in range(1, n - 1):
        i = j - 1; k = j + 1
        # n  = 1000
        # j = 100
        # i = 99
        # k = 101
        while i>=0 and n>k:
            if primes[j] - primes[i] < primes[k] - primes[j]:
                # Advance in the left list
                i-= 1
            elif primes[j] - primes[i] > primes[k] - primes[j]:
                # Advance in the right list
                k+= 1
            else:
                #print (primes[i], primes[j], primes[k])
                if son_permutaciones(primes[i], primes[j], primes[k]):
                    print("Son permutaciones:",primes[i], primes[j], primes[k])
                i-= 1; k+= 1
                

cota = 10000
result = get_primes(cota)
main(result)