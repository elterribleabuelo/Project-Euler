import math
palabras = []
count = 0

with open('words.txt', 'r') as archivo:
    # Lee el contenido línea por línea
    for linea in archivo:
        
        # Divide la línea en palabras separadas por comillas
        _palabras = linea.strip().split(',')
        
        # Filtra las palabras que no están vacías (entre las comillas)
        for _palabra in _palabras:
            palabra_sin_comillas = _palabra.strip().strip('"')
            palabras.append(palabra_sin_comillas)


for palabra in palabras:
    sum = 0
    #print("palabra:",palabra)
    for letra in palabra:
        sum += ord(letra) - ord("A") + 1
        #print("La posicion de {} en el alfabeto es {}".format(letra, ord(letra)-ord("A")+1))
    #print("sum:",sum)

    if (type(math.sqrt(8*sum + 1) == int)) and ((math.sqrt(8*sum + 1) - 1) % 2 == 0):
        count +=1

print("Cantidad de numeros triangulares en el archivo:",count)