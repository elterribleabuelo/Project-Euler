def is_palindromic(number):
    
    is_palindromic = False
    number_str = ''.join(map(str, str(number)))
    number_str_left_to_right = list(number_str)
    number_str_right_to_left = number_str[::-1]
    
    for left,right in zip(number_str_left_to_right,number_str_right_to_left):
        if left !=right:
            is_palindromic = False
            break
        else:
            is_palindromic = True
    
    return is_palindromic

def main(n):
    palindromos = []
    
    for i in range(pow(10,n),pow(10,n+1)):
        for j in range(pow(10,n),pow(10,n+1)):
            producto = i*j
            if is_palindromic(producto):
                palindromos.append(producto)
    
    maximo = max(palindromos)

    print("El máximo número palindrómico formado por la multiplicación de 2 número de tres cifras es: {}".format(maximo))
    
    return maximo

main(2)