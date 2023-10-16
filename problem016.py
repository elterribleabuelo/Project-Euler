import sys

sys.setrecursionlimit(3000)

def main(number):
    i = number - 1
    if i == 0:
        return 2
    else:
        #print(number)
        return 2 * main(i)

solve = main(1000)
print(sum(list(map(int, str(solve).strip()))))