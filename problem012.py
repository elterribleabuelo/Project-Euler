import math

def obtener_num_divisores(position):
    number = position*(position + 1) // 2
    num_div = 0
    for i in range(1,math.isqrt(number) + 1):
        if number%i == 0:
            num_div += 1
            q = number//i
            if i != q: # cuadrado
                num_div += 1
    return num_div


def main(MAX_NUM_DIVISORS):
    position = 1
    print("Buscando...")
    while obtener_num_divisores(position) <= MAX_NUM_DIVISORS:
        position +=1
    number_found = position*(position+1) // 2
    print("Fin...")
    return number_found

print(main(500))


