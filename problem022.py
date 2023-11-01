palabras = []
sum_total = 0

with open('names.txt', 'r') as archivo:
    for linea in archivo:
        _palabras = linea.strip().split(',')
        for _palabra in _palabras:
            palabra_sin_comillas = _palabra.strip().strip('"')
            palabras.append(palabra_sin_comillas)

print("len palabras:",len(palabras))

for p,palabra in enumerate(sorted(palabras)):
    sum = 0
    for letra in palabra:
        sum += ord(letra) - ord("A") + 1
    sum_total += (p+1)*sum

print("sum_total:",sum_total)