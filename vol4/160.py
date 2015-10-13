MOD = 1000000
REM = 1
for i in range(3, MOD):
    if i % 2 != 0 and i % 5 != 0:
        REM = REM * i % MOD

def count_factor(n, f):
    ret = 0
    div = f
    while n >= div:
        ret += n / div
        div *= f
    return ret

def even_factorize(n):
    if n == 0:
        return 1
    else:
        return factorize(n / 2)

def odd_factorize_coprime(n):
    ret = pow(REM, n / MOD, MOD)
    n %= MOD
    for i in range(3, n + 1):
        if i % 2 != 0 and i % 5 != 0:
            ret = ret * i % MOD
    return ret

def odd_factorize(n):
    if n == 0:
        return 1
    else:
        return odd_factorize(n / 5) * odd_factorize_coprime(n) % MOD

def factorize(n):
    return even_factorize(n) * odd_factorize(n) % MOD

def solve(n):
    twos = count_factor(n, 2) - count_factor(n, 5)
    return factorize(n) * pow(2, twos, MOD) % MOD

if __name__ == "__main__":
    print solve(10 ** 12) 
