# =============================================================================
# Los factores primos de 13195 son 5, 7, 13 y 29.
# ¿Cuál es el factor primo más grande del número 600851475143? 
# =============================================================================

factores = []
def imprimir_factores_primos(numero):
    factor = 2
    while factor <= numero:
        if numero % factor == 0:
            factores.append(factor)
            numero = numero / factor
        else:
            factor += 1
    return max(factores)

imprimir_factores_primos(600851475143)