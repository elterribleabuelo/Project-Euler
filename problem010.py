import  math

def isPrime(N):
    for i in range(2,math.isqrt(N) + 1):
        if N%i == 0:
            return False
    return True

def main(umbral):
    numers_primes = [2]
    p = 1
    suma = 2
    while(numers_primes[len(numers_primes) - 1] < umbral):
        N = 2*p + 1
        if(isPrime(N) and N < umbral):
            numers_primes.append(N)
            suma = suma + N
        if N>=umbral:
            break
        p += 1
    #print("numers_primes:",numers_primes)
    return suma

umbral = 2000000
result = print(main(umbral))