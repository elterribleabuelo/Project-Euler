import itertools

def criba_eratostenes(n):
  primes = []
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      primes.append(i)
      multiplos.update(range(i*i, n+1, i))
  return primes
  #print("Primes:",primes)


def main(N):
  
  primes = criba_eratostenes(pow(10,N))
  primes_trunqables = []
  

  for num_digits in range(2,N+1):

    listas_generadas = []

    for i in range(num_digits): # N = 5

        if i == 0:
            listas_generadas.append([2,3,5,7])
        elif i == num_digits-1:
            listas_generadas.append([3,7])
        else:
            listas_generadas.append([1,3,7,9])

    #print("listas_generadas:",listas_generadas)
    
    
    for combination in itertools.product(*listas_generadas):
        #print("combination:",combination)
        i = 0
        numero = 0
        
        while i != num_digits:
            numero += combination[i] * pow(10,num_digits-i-1)
            i = i +1
        
        if numero in primes:
        #print("1.numero:",numero)
            len_numero = len(str(numero))
            count = 1
        #print("len_numero:",len_numero)
        
            for j in range(1,len_numero):

                number_trunqable_left = int(str(numero)[0:len_numero-j])
                
                number_trunqable_right = int(str(numero)[j:len_numero])

                if number_trunqable_left in primes and number_trunqable_right in primes:
                    count +=1
                    if count == len_numero:
                        #print("Primo truncable por izq y der:",numero)
                        primes_trunqables.append(numero)
  
  print("primes_trunqables:",primes_trunqables)
  
  if len(primes_trunqables):
    suma = sum(primes_trunqables)
    print("La suma es:",suma)

  


main(6)