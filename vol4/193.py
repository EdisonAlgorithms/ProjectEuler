import math

if __name__ == "__main__":
    L = 2 ** 50
    sL = int(math.sqrt(L))
    div = [0] * sL
    for i in xrange(2, sL):
        if div[i] != 0:
            continue
        for j in xrange(i * i, sL, i * i):
            div[j] = -1
        for j in xrange(i, sL, i):
            if div[j] != -1:
                div[j] += 1 
    total = 0
    for i in xrange(2, sL):
        if div[i] == -1:
            continue
        if div[i] % 2 == 0:
            total -= L / (i * i)
        else:
            total += L / (i * i)
    print L - total
