import math
from fractions import Fraction, gcd

N = 10 ** 5
L = 10 ** 12

def solve(n):
    a = [1, (n + 1)]
    b = [1, 2]
    while b[-1] / gcd(a[-1], b[-1]) <= L:
        a.append(2 * a[-1] + (n - 1) * a[-2])
        b.append(2 * b[-1] + (n - 1) * b[-2])
    f1 = Fraction(a[-2], b[-2])
    f2 = Fraction(a[-3], b[-3])
    mean = (f1 + f2) / 2
    if mean * mean < n:
        f = max(f1, f2)
    else:
        f = min(f1, f2)
    return f.denominator

if __name__ == "__main__":
    ans = 0
    for n in range(2, N + 1):
        print n
        s = int(math.sqrt(n))
        if s * s != n:
            ans += solve(n)
    print ans

