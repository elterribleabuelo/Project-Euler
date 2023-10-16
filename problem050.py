import  math

def isPrime(N):
    if N < 2:
        return False
    for i in range(2,math.isqrt(N) + 1):
        if N%i == 0:
            return False
    return True

def get_primes(cota):
    numers_primes = []

    for number in range(cota):
        if(isPrime(number)):
            numers_primes.append(number)
    
    print("numers_primes:",numers_primes)

    return numers_primes

def main(primes,cota):

    max_len_sequence = 0
    
    for i in range(0,len(primes)):
        
        #print("Secuencia comenzando desde:",primes[i])
        
        sum = 0

        sum_primes = []
        
        for j in range(i,len(primes)):
            
            sum += primes[j]

            sum_primes.append(primes[j])
            
            if isPrime(sum) and sum<=cota and len(sum_primes)>1:
                len_secuence = len(sum_primes)
                if len_secuence > max_len_sequence:
                    max_len_sequence = len_secuence
                    print("Suma:",sum)
                    print("len_secuence:",len_secuence)
            if sum>cota:
                break

cota = 1000000
result = get_primes(cota)
main(result,cota) # 997651