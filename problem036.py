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

def convert_number_in_base_n(number,n):
    digits_number_in_base_n = []

    if number == 1:
        digits_number_in_base_n = [1]
        digits_number_in_base_n = digits_number_in_base_n[::-1]
        number_str = ''.join(list(map(str, digits_number_in_base_n)))
        return number_str
    
    while number >=n:
        resto = number % n
        q = number // n 
        digits_number_in_base_n.append(resto)
        if q < n:
            digits_number_in_base_n.append(q)
        number = number // n
    digits_number_in_base_n = digits_number_in_base_n[::-1]
    number_str = ''.join(list(map(str, digits_number_in_base_n)))
    return number_str

def main(MAX):
    sum = 0
    for number in range(1,MAX):
        if (is_palindromic(number) and is_palindromic(convert_number_in_base_n(number,2))):
            sum += number
    print("La suma de todos los numeros palindomicos de 1 hasta {} es : {}".format(MAX,sum))
    return sum
    
main(1000000)