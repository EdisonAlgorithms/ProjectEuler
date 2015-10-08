def tetration(a, b, m):
    t0 = 1
    for i in range(b):
        t1 = pow(a, t0, m)
        if t0 == t1:
            break
        t0 = t1
    return t0

if __name__ == "__main__":
    print tetration(1777, 1855, 10 ** 8)
