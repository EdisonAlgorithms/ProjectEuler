import math

MOD = 10 ** 9
L = 20

if __name__ == "__main__":
    f = {1: {}}
    for i in range(1, 10):
        f[1][i * i] = (i, 1)
    for i in range(2, L + 1):
        f[i] = {}
        for s in range(1, (i - 1) * 81 + 1):
            if s in f[i - 1]:
                for j in range(10):
                    s0, c0 = f[i - 1][s]
                    s1, c1 = f[i].get(s + j * j, (0, 0))
                    f[i][s + j * j] = ((s1 + s0 * 10 + j * c0) % MOD, (c1 + c0) % MOD)
    ans = 0
    for i in range(1, L + 1):
        for j in range(1, int(math.sqrt(i * 81)) + 1):
            ans = (ans + f[i].get(j * j, (0, 0))[0]) % MOD
    print ans
