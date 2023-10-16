def collatzUtil(number,lookup):

    if number in lookup:
        return lookup[number]

    if number == 1:
        lookup[number] = 1
        return lookup[number]

    elif number%2==0: 
        _number = number // 2
        lookup[number] = 1 + collatzUtil(_number,lookup)
        return lookup[number]
    
    else:
        _number = 3*number + 1
        lookup[number] = 1 + collatzUtil(_number,lookup)
        return lookup[number]
    


def collatzLen(N):
    
    lookup = {}

    max_long_collatz = 1

    k_number = 0

    collatzUtil(N,lookup)

    for number in range(1,N):
        if number not in lookup:
            collatzUtil(number,lookup)
        
        long_collatz_number = lookup[number]

        if long_collatz_number > max_long_collatz:
            max_long_collatz = long_collatz_number
            k_number = number

    print(k_number,max_long_collatz)
    return (k_number,max_long_collatz)

collatzLen(1000000)