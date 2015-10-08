def sieve_primes(n):
    p = [0] * (n + 1)
    ret = []
    for i in range(2, n + 1):
        if p[i] == 0:
            for j in range(2 * i, n + 1, i):
                p[j] = 1
            ret.append(i)
    return ret

def get_mods(n):
    add = [1, 3, 7, 9, 13, 27]
    ret = [True] * n
    for i in range(n):
        for j in add:
            if (i * i + j) % n == 0:
                ret[i] = False
                break
    return ret

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

# Miller-Rabin Test
def is_prime(n):
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

if __name__ == "__main__":
    L = 150 * (10 ** 6)
    prime = sieve_primes(5000)
    mods = []
    for p in prime:
        mods.append(get_mods(p))
    
    ans = 0
    for i in xrange(10, L, 10):
        ok = True
        
        for j in xrange(len(prime)):
            if i * i < prime[j]:
                break
            if not ok:
                break
            ok = mods[j][i % prime[j]]
        
        add = [1, 3, 7, 9, 13, 27]
        for j in add:
            if not ok:
                break
            ok = is_prime(i * i + j)

        not_add = [19, 21]
        for j in not_add:
            if not ok:
                break
            ok = not is_prime(i * i + j)

        if ok:
            ans += i
    
    print ans
