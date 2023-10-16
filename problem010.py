import  math

def isPrime(N):
    for i in range(2,math.isqrt(N)):
        if N%i == 0:
            return False
    
    return True

def main(umbral):
    numers_primes = [2]
    p = 1
    suma = 0
    while(max(numers_primes) <= umbral):
        N = 2*p + 1
        if(isPrime(N)):
            suma = suma + N
        p += 1
    return suma

umbral = 2000000
result = main(umbral)

print("La suma es :", result) # 23514624000