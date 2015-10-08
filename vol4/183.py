import math
import fractions

def calc_d(n):
    k = round(n / math.e)
    d = fractions.gcd(n, k)
    k /= d
    while k % 2 == 0:
        k /= 2
    while k % 5 == 0:
        k /= 5
    if k == 1:
        return -n
    else:
        return n

if __name__ == "__main__":
    L = 10000
    ans = 0
    for n in range(5, L + 1):
        ans += calc_d(n)
    print ans
