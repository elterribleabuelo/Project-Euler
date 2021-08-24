# =============================================================================
# Si enumeramos todos los números naturales por debajo de 10 que son múltiplos de 3 o 5, 
# obtenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23.
# Encuentra la suma de todos los múltiplos de 3 o 5 por debajo de 1000.
# =============================================================================

suma = 0
for i in range(0,1000):
    if i%3==0 or i%5 ==0:
        suma = suma + i
print(suma)
