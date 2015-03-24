if __name__ == "__main__":
    L = 50 * (10 ** 6)
    p = [0] * L
    prime = []
    for i in range(2, L):
        if p[i] == 0:
            for j in range(2 * i, L, i):
                p[j] = 1
            prime.append(i)
    ans = 0 # for n = 4 and 16
    for i in p:
        if i * 4 < L:
            ans += 1
        if i * 16 < L:
            ans += 1
        if (i - 3) % 4 == 0:
            ans += 1
    print ans
