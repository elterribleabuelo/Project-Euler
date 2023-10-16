import  math

def isPrime(N):
    if N < 2:
        return False
    for i in range(2,math.isqrt(N) + 1):
        if N%i == 0:
            return False
    return True

def main(position):
    numers_primes = []
    p = 0
    while(len(numers_primes) <= position):
        N = 2*p + 1
        if(isPrime(N)):
            numers_primes.append(N)
        p+=1
    return numers_primes

position = 10001
result = main(position)

print(result[position - 1])


