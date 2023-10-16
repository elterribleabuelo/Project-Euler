def obtener_num_divisores(N):
    #print("Funcion obtener numero de divisores del numero",N)
    num_div = 0
    for i in range(1,N+1):
        if N%i == 0:
            num_div +=1
    #print("====num_div===",num_div)
    return num_div


def sumatoria_triangular(num):
    print("Valor inicial ->",num)
    print("sacando divisores")
    if num > 1:
        num = num  +  sumatoria_triangular(num  - 1)
        print("valor final ->",num)
        if obtener_num_divisores(num)==7:
            print("Numero obtenido:",num)
            return
        
    #print("###")
    return num


def main(num,MAX_NUM_DIVISORS):
    print("Valor inicial ->",num)
    while obtener_num_divisores(num) < MAX_NUM_DIVISORS:
        num = num + main(num  + 1,MAX_NUM_DIVISORS)
        print("valor final ->",num)
        break
    return num

print(sumatoria_triangular(50))


