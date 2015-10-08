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
    count = 1
    LIMIT = 2000
    n = 0
    while count < LIMIT:
        n += 1
        if is_prime(6 * n - 1) and is_prime(6 * n + 1) and is_prime(12 * n + 5):
            count += 1
            number = 3 * n * n - 3 * n + 2
            if count == LIMIT:
                break
        if is_prime(6 * n - 1) and is_prime(6 * n + 5) and is_prime(12 * n - 7) and n > 1:
            count += 1
            number = 3 * n * n + 3 * n + 1
            if count == LIMIT:
                break
    print number
