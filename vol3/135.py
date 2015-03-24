if __name__ == "__main__":
    L = 10 ** 6
    sol = [0] * (L + 1)
    for u in xrange(1, L + 1):
        for v in xrange(1, L + 1):
            if u * v > L:
                break
            if 3 * v <= u:
                continue
            if (u + v) % 4 == 0 and (3 * v - u) % 4 == 0:
                sol[u * v] += 1
    ans = 0
    for i in range(1, L + 1):
        if sol[i] == 10:
            ans += 1
    print ans
