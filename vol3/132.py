if __name__ == "__main__":
    LIMIT = 20 ** 5
    is_prime = [1] * (LIMIT + 1)
    k = 10 ** 9
    count = 0
    ans = 0
    for i in range(2, LIMIT + 1):
        if is_prime[i] == 0:
            continue
        for j in range(i, LIMIT + 1, i):
            is_prime[j] = 0
        if pow(10, k, 9 * i) == 1:
            count += 1
            ans += i
        if count == 40:
            break
    print count, ans
