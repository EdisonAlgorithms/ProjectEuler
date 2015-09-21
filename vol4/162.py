from operator import mul
from fractions import Fraction

def nCk(n,k): 
    return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

def nPk(n, k):
    return int(reduce(mul, (n - i for i in range(k)), 1))

if __name__ == "__main__":
    L = 16
    ans = 0
    for i in range(3, L + 1):
        ans += 15 * 16 ** (i - 1) + 41 * 14 ** (i - 1) - (43 * 15 ** (i - 1) + 13 ** i)
    print '%X' % ans
