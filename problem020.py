def factorial(num):
    if num <=1:
        return num
    else:
        return num*factorial(num-1)

def main(num):
    number = factorial(num)
    number_str = str(number)
    digits = []

    for k in range(0,len(str(number))):
        digits.append(int(number_str[k]))
    print("suma de digitos:",sum(digits))

main(100)