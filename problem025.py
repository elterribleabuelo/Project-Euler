import sys
sys.setrecursionlimit(1000000)

def fib(n, lookup,result):
 
    if n <= 1:
        return n
    
    if n not in lookup:
        val = fib(n - 1, lookup, result) + fib(n - 2, lookup, result)
        number_digits = len(str(val))
        lookup[n] = val
        if number_digits == 1000:
            result.append(n)
    return lookup[n]


def main(input):
    lookup = {}
    result = []
    fib(input, lookup,result)
    print("Indice de primer numero con 1000 digitos:",result[0])
    return

input = 5000

main(input)