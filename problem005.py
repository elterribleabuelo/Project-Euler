from functools import reduce

def multiplicar(x, y):
    return x * y

def criba_eratostenes(n):
  primes = []
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      primes.append(i)
      multiplos.update(range(i*i, n+1, i))
  return primes


def main(limit_sup):
    list_divisors = list(range(1, limit_sup + 1))
    list_primes = criba_eratostenes(limit_sup)
    cota_inferior = reduce(multiplicar, list_primes)
    found = False
    while found == False:
        count = 0
        for divisor in list_divisors:
            if cota_inferior % divisor == 0:
                count +=1
        if count == len(list_divisors):
            found = True
            print("El menor numero con divisores desde el 1 hasta el {} es:{}".format(limit_sup,cota_inferior))
            break
        else:
            cota_inferior +=10
    return cota_inferior

print(main(20))