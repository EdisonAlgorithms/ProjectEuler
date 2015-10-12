import itertools
import time

def digits(n):
    while n:
        yield n % 10
        n /= 10

def pows(b):
    x = 1
    while True:
        yield x
        x *= 10

def f(n, d):
    def g(d0, m):
        if d0 < d:
            return n / (m * 10) * m
        elif d0 == d:
            return n / (m * 10) * m + n % m + 1
        else:
            return (n / (m * 10) + 1) * m 

    return sum(itertools.starmap(g, itertools.izip(digits(n), pows(10))))

def solve(L, d):
    n = 1
    ret = 0
    while True:
        m = f(n, d)
        if m == n:
            ret += n
            n += 1
        elif m < n:
            n += max(1, (n - m) / (sum(1 for _ in digits(n)) + 1))
        else:
            if m - n >= L:
                break
            n += m - n
    return ret

if __name__ == "__main__":
    L = 10 ** 100
    t0 = time.clock()
    print sum(solve(L, d) for d in range(1, 10))
    t1 = time.clock()
    print 'time = ', t1 - t0