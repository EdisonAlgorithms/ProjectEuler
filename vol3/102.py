import urllib2

if __name__ == "__main__":
    ans = 0
    for line in urllib2.urlopen('https://projecteuler.net/project/resources/p102_triangles.txt'):
        ax, ay, bx, by, cx, cy = map(int, line.split(','))
        a = ax * by - ay * bx > 0
        b = bx * cy - by * cx > 0
        c = cx * ay - cy * ax > 0
        ans += a == b == c
    print ans
