import math

def champernowne(n) :
    
    champ = ""
    i = 0
    j = 0
    digits = []
    
    while len(champ)<n :
        i = i + 1
        champ = champ + str(i)

    for k in range(1,len(champ)):
        exponente = math.log10(k)
        if exponente.is_integer():
            digits.append(champ[k-1]) 
    
    print("digits:",digits) # ['1', '1', '5', '3', '7', '2', '1']
    
    return digits

champernowne(1000000)