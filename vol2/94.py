if __name__ == "__main__":
    s0, s1, p = 1, 1, 0
    m = 1
    ans = 0
    LIMIT = 10 ** 9
    while p < LIMIT:
        s0, s1, m = s1, 4 * s1 - s0 + 2 * m, -m
        ans += p
        p = 3 * s1 - m
    print ans
