def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if __name__ == "__main__":
    LIMIT = 10 ** 6
    i = 1
    ans = 0
    while True:
        p = ((i + 1) ** 3) - (i ** 3)
        if p > LIMIT:
            break
        if is_prime(p):
            ans += 1
        i += 1
    print ans
