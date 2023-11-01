def main():
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

main()