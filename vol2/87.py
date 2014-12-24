import math

if __name__ == "__main__":
    L = 50000000
    N = int(math.sqrt(L))
    p = [0] * (N + 1)
    primes = []
    for i in range(2, N):
        if p[i] == 0:
            primes.append(i)
            for j in range (2, N / i + 1):
                p[i * j] = 1
    s = set()
    for i in primes:
        for j in primes:
            s1 = i ** 4 + j ** 3
            if s1 >= L:
                break
            for k in primes:
                s2 = s1 + k ** 2
                if s2 >= L:
                    break
                s.add(s2)
    print len(s)

