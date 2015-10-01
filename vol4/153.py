import math
import fractions

if __name__ == "__main__":
    L = 10 ** 8
    ans = 0
    for i in xrange(1, L + 1):
        ans += (L / i) * i
        if i * i < L:
            j = 1
            while j <= i:
                if fractions.gcd(i, j) == 1:
                    div = i * i + j * j
                    k = 1
                    v = 2 * i if i == j else 2 * (i + j)
                    while div * k <= L:
                        ans += (L / (div * k)) * k * v
                        k += 1
                j += 1
    print ans
