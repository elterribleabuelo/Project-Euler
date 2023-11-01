def main(N):
    lookup = {}
    for number in range(2,N+1):
        divisor = number
        periodic_number = []
        rest_number = []
        dividendo = 10
        resto = 0
        while (resto not in rest_number) or (dividendo!=0):
            if dividendo < divisor:
                if dividendo == 0:
                    break
                else:
                    dividendo = dividendo * 10
                    if dividendo < divisor:
                        periodic_number.append(0)
                    else:
                        cociente = dividendo // divisor
                        resto = dividendo % divisor
                        dividendo = resto
                        if resto not in rest_number:
                            periodic_number.append(cociente)
                            rest_number.append(resto)
                        else:
                            break
            else:
                if dividendo!=0:
                    cociente = dividendo // divisor
                    resto = dividendo % divisor
                    dividendo = resto
                    periodic_number.append(cociente)
                    rest_number.append(resto)
                else:
                    print("Se termino la operacion")
            lookup[number] = periodic_number
    clave_con_max_longitud = max(lookup, key=lambda clave: len(lookup[clave]))
    print(f"El numero entre 2 y 1000 con la secuencia más grande de decimales es: {clave_con_max_longitud}")
    print(f"Su secuencia es: {lookup[clave_con_max_longitud]}")
    return lookup

response = main(1000) # 983        