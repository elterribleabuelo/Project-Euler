# =============================================================================
# Un número palindrómico se lee igual en ambos sentidos. 
# El palíndromo más grande hecho del producto de dos números de 2 dígitos es 9009 = 91 × 99.

# Encuentra el palíndromo más grande formado por el producto de dos números de 3 dígitos.
# =============================================================================

def max_palindromos(n):
    palindromos = []
    for i in range(pow(10,n),pow(10,n+1)):
        for j in range(pow(10,n),pow(10,n+1)):
            producto = i*j
            comparacion = str(producto)
            longitud = len(comparacion)
            count = 0
            if longitud %2 == 1:
                for k in range((longitud-1)//2):
                    if comparacion[k] == comparacion[longitud-1-k]:
                        count = count + 1
                if count == (longitud-1)//2:
                    palindromos.append(producto)
            else :
                for k in range(longitud//2):
                    if comparacion[k] == comparacion[longitud-1-k]:
                        count = count + 1
                if count == longitud//2:
                    palindromos.append(producto)
    maximo = max(palindromos)
    
    return maximo

max_palindromos(2)            