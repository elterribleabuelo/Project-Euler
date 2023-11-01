def main():
    suma = 0
    for i in range(0,1000):
        if i%3==0 or i%5 ==0:
            suma = suma + i
    print(suma)
    return suma

main()

