def main(num):
    if num == 1:
        return 1
    else:
        if num % 10 !=0:
            ultimos_10_digits = (pow(num,num) + main(num-1))%pow(10,10)
            return ultimos_10_digits
        else:
            num = num - 1
            ultimos_10_digits = (pow(num,num) + main(num-1))%pow(10,10)
            return ultimos_10_digits

print(main(1000))