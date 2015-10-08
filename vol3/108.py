def getPrimes(n):
    ret = []
    d = [0] * (n + 1)
    for i in range(2, n + 1):
        if d[i] == 0:
            for j in range(2 * i, n, i):
                d[j] = 0
            ret.append(i)
    return ret

def calc(n, p):
    ret = 1
    r = n
    for i in p:
        if i * i > n:
            return ret * 2 
        e = 1
        while r % i == 0:
            e += 2
            r = r / i
        ret *= e
        if r == 1:
            return ret
    return ret


if __name__ == "__main__":
    L = 200000
    p = getPrimes(L)
    n = 4
    while (calc(n, p) + 1) / 2 <= 1000:
        n += 1
    print n
