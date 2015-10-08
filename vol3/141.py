import math

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def is_square(n):
    sqrt_n = int(math.sqrt(n))
    return n == sqrt_n * sqrt_n

if __name__ == "__main__":
    L = 10 ** 12
    s = set()
    for a in xrange(2, 10000):
        for b in xrange(1, a):
            if a * a * a * b + b * b >= L:
                break
            if gcd(a, b) > 1:
                continue

            c = 1
            while True:
                n = a * a * a * b * c * c + b * b * c
                if n >= L:
                    break
                if is_square(n):
                    s.add(n)
                c += 1
    print sum(s)
