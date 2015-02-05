from fractions import gcd

if __name__ == "__main__":
    LIMIT = 120000
    rad = [1] * LIMIT
    for i in range(2, LIMIT):
        if rad[i] == 1:
            for j in range(i, LIMIT, i):
                rad[j] *= i
    ele = []
    for i in range(1, LIMIT):
        ele.append([rad[i], i])
    ele = sorted(ele)

    ans = 0
    for c in range(3, LIMIT):
        chalf = c / 2
        for [ra, a] in ele:
            if ra * rad[c] > chalf:
                break
            b = c - a
            if a >= b:
                continue
            if ra * rad[b] * rad[c] >= c:
                continue
            if gcd(ra, rad[b]) != 1:
                continue
            ans += c
    print ans
