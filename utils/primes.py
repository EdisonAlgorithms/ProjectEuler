#################################################
# Eratosthenes_Sieve
#################################################
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

#################################################
# Miller-Rabin Test
#################################################
def witness(a, n):
    t = 0
    u = n - 1
    while u % 2 == 0:
        t += 1
        u /= 2
    
    x = pow(a, u, n)
    if x == 1 or x == n - 1:
        return False
    for i in range(t - 1):
        x = x * x  % n
        if x == 1:
            return True
        if x == n - 1:
            return False
    return True

def is_prime_array(n, array):
    for a in array:
        if witness(a, n):
            return False
    return True

def is_prime(n):
    if n == 0:
        return False
    if n < 1373653:
        return is_prime_array(n, [2, 3])
    elif n < 9080191:
        return is_prime_array(n, [31, 73])
    elif n < 4759123141:
        return is_prime_array(n, [2, 7, 61])
    elif n < 2152302898747:
        return is_prime_array(n, [2, 3, 5, 7, 11])
    elif n < 3474749660383:
        return is_prime_array(n, [2, 3, 5, 7, 11, 13])
    else:
        return is_prime_array(n, [2, 3, 5, 7, 11, 13, 17])