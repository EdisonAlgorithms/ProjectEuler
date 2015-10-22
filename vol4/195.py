from math import sqrt
from fractions import gcd

def solve(r):
    ret = 0
    M = int(r * 2 * 3 / sqrt(3))
    for m in xrange(2, M + 1):
        for n in xrange(1, m):
            if gcd(m, n) != 1:
                continue
            a = (m + 2 * n) * m
            b = (n + 2 * m) * n
            c = m * m + m * n + n * n
            d = gcd(a, gcd(b, c))
            if sqrt(3) * m * n / 2 / 3 > r:
                break
            ret += int(r / (sqrt(3) * m * n / 2 / d))
    return ret

if __name__ == "__main__":
    ans = solve(1053779)
    print ans
