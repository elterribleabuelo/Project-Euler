from itertools import permutations

def main(numeros):
    permutaciones = permutations(numeros)
    numeros_generados = [''.join(map(str, perm)) for perm in permutaciones]
    #numeros_generados = list(map(int, numeros_generados))
    #numeros_generados = sorted(numeros_generados)
    primes = [2,3,5,7,11,13,17]
    sum_num_pandigital = 0
    
    for numero in numeros_generados:
        #print("numero:",numero)
        sub_numeros = []
        cnt = 0
        for i in range(0,9):
            if i>=1 and i<=7:
                #print("sub_numero:",str(numero)[i:i+3])
                sub_numeros.append(int(str(numero)[i:i+3]))
        
        #print("sub_numeros:",sub_numeros)
        
        for number,prime in zip(sub_numeros,primes):
            #print("number,prime:",number,prime)
            if number%prime == 0:
                cnt +=1
        if cnt == 7:
            sum_num_pandigital +=int(numero)
            #print("numero:",numero)
        #print("subnumeros:",sub_numeros)
        #break
    print("Suma de numeros pandigitales:",sum_num_pandigital)


main('0123456789')