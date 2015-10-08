def prodsum(p, s, c, start):
    k = p - s + c
    if k < LIMIT:
        if p < ans[k]: ans[k] = p
        for i in range(start, LIMIT // p * 2):
            prodsum(p * i, s + i, c + 1, i)

LIMIT = 12000
ans = [2 * LIMIT] * LIMIT
prodsum(1, 1, 1, 2)
print sum(set(ans[2:]))
