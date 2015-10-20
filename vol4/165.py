from fractions import Fraction
import time

def gen_random():
    s = 290797
    while True:
        s = (s * s) % 50515093
        t = s % 500
        yield int(t)

# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
def calc_intersect(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    D = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if D == 0:
        return False

    s = (y4 - y3) * (x3 - x1) - (x4 - x3) * (y3 - y1)
    t = (y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)

    if D > 0:
        if 0 < s and s < D and 0 < t and t < D:
            s = Fraction(s, D)
        else:
            return False
    else:
        if 0 < -s and -s < -D and 0 < -t and -t < -D:
            s = Fraction(s, D)
        else:
            return False

    return (x1 + s * (x2 - x1), y1 + s * (y2 - y1))

if __name__ == "__main__":
    t0 = time.clock()
    
    N = 5000
    lines = []
    g = gen_random()
    for k in range(N):
        x1, y1 = g.next(), g.next()
        x2, y2 = g.next(), g.next()
        l = (x1, y1, x2, y2)
        lines.append(l)

    intersections = set()
    for i in xrange(N):
        if i % 100 == 0:
            print i
        for j in xrange(i + 1, N):
            pt = calc_intersect(lines[i], lines[j])
            if pt:
                intersections.add((pt[0].numerator, pt[0].denominator, pt[1].numerator, pt[1].denominator))

    ans = len(intersections)
    print ans

    t1 = time.clock()
    print t1 - t0
