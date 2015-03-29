from itertools import *

def product(a):
    return reduce(lambda x, y: x * y, a, 1)

if __name__ == "__main__":
    L = 10 ** 9
    number = []
    while L > 0:
        number.append(L % 7)
        L /= 7
    ans = 0
    carry = 1
    for i in range(len(number)):
        par_sum = number[i] * (number[i] + 1) / 2
        ans += pow(28, i) * par_sum * product(d + 1 for d in number[i + 1:])

    print ans
    
