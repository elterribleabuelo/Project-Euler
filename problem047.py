import  math
from tqdm import tqdm

upper_limit = 500000
factors_list = [0] * upper_limit

def main():
    for i, j in enumerate(factors_list):
        if i in [0, 1]:
            continue
        if factors_list[i] == 0:
            for k in range(i, upper_limit, i):
                factors_list[k] += 1
        if factors_list[i] == 4:
            if factors_list[i - 1] == factors_list[i - 2] == factors_list[i - 3] == 4:
                print(i - 3)
                break
    pass
main()
"""def isPrime(N):
    if N < 2:
        return False
    for i in range(2,math.isqrt(N) + 1):
        if N%i == 0:
            return False
    return True

def get_factor_primes(cota):
    factors_primes = []

    for number in range(2,cota):
        #print("cota,number:",cota,number)
        if cota !=1:
            if(isPrime(number) and cota % number == 0):
                #print("number:",number)
                cota = cota // number
                while cota % number == 0:
                    cota = cota // number
                factors_primes.append(number)
        else:
            break
            
    
    #print("factors_primes:",factors_primes)

    return factors_primes

def main(exp):
    
    for number in tqdm(range(pow(10,exp),pow(10,exp+1))):
        
        factors_primes_x = set(get_factor_primes(number))
        #print("factors_primes_x:",len(factors_primes_x))
        factors_primes_y = set(get_factor_primes(number + 1))
        #print("factors_primes_y:",len(factors_primes_y))
        factors_primes_z = set(get_factor_primes(number + 2))
        #print("factors_primes_z:",len(factors_primes_z))
        factors_primes_w = set(get_factor_primes(number + 3))

        if (len(factors_primes_x) == 4) and (len(factors_primes_y) == 4) and (len(factors_primes_z) == 4) and (len(factors_primes_w) == 4):
            
            #print("factors_primes_x:",len(factors_primes_x))
            #print("factors_primes_y:",len(factors_primes_y))
            #print("factors_primes_z:",len(factors_primes_z))

            if factors_primes_x.isdisjoint(factors_primes_y) and factors_primes_y.isdisjoint(factors_primes_z) and factors_primes_z.isdisjoint(factors_primes_w):
                print("factors_primes_x:",factors_primes_x)
                print("factors_primes_y:",factors_primes_y)
                print("factors_primes_z:",factors_primes_z)
                print("factors_primes_w:",factors_primes_w)
                print(number,number+1,number+2,number+3)
                break

#cota = 90
#result = get_factor_primes(cota)

main(5)"""