from utils import get_primes

if __name__ == "__main__":
    L = 10 ** 8
    primes = get_primes(L / 2)
    ans = 0
    for i in xrange(0, len(primes)):
        if primes[i] >= 10000:
            break
        for j in xrange(i, len(primes)):
            if primes[i] * primes[j] > L:
                break
            ans += 1
    print primes[-1]
    print ans
