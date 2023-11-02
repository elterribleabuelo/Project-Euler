import math

def get_factores(number):
    divisors = [1]
    for i in range(2,math.isqrt(number) + 1):
        if number % i == 0:
            divisors.append(i)
            q = number // i
            if q !=i:
                divisors.append(q)
    return divisors

def is_amicable(number):
    sum_divisors_own_a = sum(get_factores(number))
    sum_divisors_own_b = sum(get_factores(sum_divisors_own_a))
    if number == sum_divisors_own_b and sum_divisors_own_a!=sum_divisors_own_b:
        return True
    else:
        return False

def main(MAX):
    numbers_amicables = []
    for number in range(1,MAX):
        if is_amicable(number):
            numbers_amicables.append(number)
    suma_amicables = sum(numbers_amicables)
    print("La suma de todos los numeros amigables menores a {} es:{}".format(MAX,suma_amicables))

main(10000)

