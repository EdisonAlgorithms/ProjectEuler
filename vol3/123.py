if __name__ == "__main__":
    is_prime = [0] * 1000001
    prime = []
    for i in range(2, 1000001):
        if is_prime[i] == 0:
            prime.append(i)
            for j in range(2 * i, 1000001, i):
                is_prime[j] = 1
    LIMIT = 10 ** 10
    n = 7037
    while True:
        n += 2
        r = 2 * prime[n - 1] * n
        if r >= LIMIT:
            break
    print n
