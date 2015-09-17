# Eratosthenes_Sieve
def get_primes(n):    
    num = [True] * (n + 1)
    i = 2
    primes = []
    while i <= n:
        if num[i] == True:
            for j in xrange(i * i, n + 1, i):
                num[j] = False
            primes.append(i)
        i += 1
    return primes
    
