def calc(a):
    s = set([2])
    for n in range(1, 2 * a + 1, 2):
        r = (2 * n * a) % (a * a)
        s.add(r)
    return max(s)

if __name__ == "__main__":
    print sum([calc(a) for a in range(3, 1001)])
