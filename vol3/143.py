def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

if __name__ == "__main__":
    L = 120000
    m = {}
    for u in xrange(1, L):
        if u * u > L:
            break
        for v in xrange(1, u):
            if gcd(u, v) != 1:
                continue
            if (u - v) % 3 == 0:
                continue

            a = 2 * u * v + v * v
            b = u * u - v * v

            if a + b > L:
                break

            for k in xrange(1, L):
                if k * (a + b) > L: 
                    break
                if a < b:
                    if m.has_key(k * a):
                        m[k * a].add(k * b)
                    else:
                        m[k * a] = set([k * b])
                else:
                    if m.has_key(k * b):
                        m[k * b].add(k * a)
                    else:
                        m[k * b] = set([k * a])

    s = set()
    for a in m.keys(): 
        for b in m[a]:
            if not m.has_key(b):
                continue
            for c in m[b]:
                if c in m[a]:
                    if a + b +c <= L:
                        s.add(a + b + c)
    print sum(s)
