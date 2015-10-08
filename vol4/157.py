from operator import mul

def factorize(x):
    ret = {}
    for i in xrange(2, x + 1):
        while x % i == 0:
            ret[i] = ret.get(i, 0) + 1
            x /= i
    return ret

def solve(n):
    ret = 0
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            # 2 ^ i, 5 ^ j
            factors = factorize(pow(2, i) + pow(5, j))
            factors[2] = factors.get(2, 0) + n - i
            factors[5] = factors.get(5, 0) + n - j
            ret += reduce(mul, map(lambda x: x + 1, factors.itervalues()))
            
            # 1, 2 ^ i * 5 ^ j
            if i == 0 or j == 0:
                continue
            factors = factorize(pow(2, i) * pow(5, j) + 1)
            factors[2] = n - i
            factors[5] = n - j
            ret += reduce(mul, map(lambda x: x + 1, factors.itervalues()))

    return ret

if __name__ == "__main__":
    ans = sum(solve(n) for n in range(1, 10))
    print ans
