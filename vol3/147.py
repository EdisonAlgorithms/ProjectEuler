def nrect(m, n):
    if m < n:
        m, n = n, m
    
    hvr = m * (m + 1) * n * (n + 1) / 4
    
    start = [0] * (m + n - 1)
    end = [0] * (m + n - 1)
    for i in xrange(m - 1, 0, -1):
        start[m - 1 - i] = i
        end[m - 1 - i] = i + 2 * min(m - i, n)
    for i in xrange(n):
        start[m - 1 + i] = i
        end[m - 1 + i] = i + 2 * min(m, n - i)
    dr = 0
    for i in xrange(m + n - 1):
        for j in xrange(i + 1, m + n - 1):
            s = max(start[i], start[j])
            e = min(end[i], end[j])
            if s < e:
                dr += (e - s) * (e - s + 1) / 2
    
    return hvr + dr

if __name__ == "__main__":
    w, h = 47, 43
    print sum(nrect(m, n) for m in xrange(1, w + 1) for n in xrange(1, h + 1))
