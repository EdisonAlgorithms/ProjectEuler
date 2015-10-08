from itertools import combinations, product

def is_prime(n):
    for i in xrange(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

def generator(n, d, rep):
    other_indexes = combinations(range(n), n - rep);
    other_numbers = product(list(set(range(10)) - set([d])), repeat = n - rep);
    for t in product(other_indexes, other_numbers):
        base = [d] * n
        for ind, val in zip(*t):
            base[ind] = val
        if base[0] == 0:
            continue
        ret = 0
        for i in range(n):
            ret = ret * 10 + base[i]
        yield ret

if __name__ == "__main__":
    n = 10
    ans = 0
    for d in range(10):
        res = []
        rep = n - 1
        while not res:
            for x in generator(n, d, rep):
                if not is_prime(x):
                    continue
                res.append(x)
            rep -= 1
        ans += sum(res)
    print ans
