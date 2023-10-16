def criba_eratostenes(n):
  primes = []
  multiplos = set()
  for i in range(2, n+1):
    if i not in multiplos:
      primes.append(i)
      multiplos.update(range(i*i, n+1, i))
  return primes

def is_circular_number(number,primes):
   
   is_circular_prime = False
   len_number = len(str(number))
   
   for i in range(1,len_number):
      
      number = str(number)[1:len_number] + str(number)[0]
      _number = int(number)
      
      if _number in primes:
        is_circular_prime = True
      else:
        is_circular_prime = False
        break
   return is_circular_prime

def main(n):
  
  primes = criba_eratostenes(n)
  count = 4 # [2,3,5,7]
  suma = 0

  for prime in primes:
    
    result = is_circular_number(prime,primes)

    if result:
      #print("primo circular:",prime)
      count += 1
      suma += prime
  
  print("Numero de primos circulares:",count)
  return

main(1000000)