# =============================================================================
# Cada nuevo término de la secuencia de Fibonacci se genera sumando los dos términos anteriores. 
# Al comenzar con 1 y 2, los primeros 10 términos serán:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Al considerar los términos en la secuencia de Fibonacci cuyos valores no exceden los cuatro millones, 
# encuentre la suma de los términos pares.
# =============================================================================

m, n = 1,2
suma = 0
suma_par = 0
while suma<=4*pow(10,6):
    suma = m + n
    m = n 
    n = suma
    if suma%2 == 0:
        suma_par = suma_par + suma

print(suma_par + 2)