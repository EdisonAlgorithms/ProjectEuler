if __name__ == "__main__":
    L = 1000
    triangle = []
    t = 0
    for i in xrange(L):
        line = []
        for j in xrange(i + 1):
            t = (615949 * t + 797807) % (2 ** 20)
            line.append(t - (2 ** 19))
        triangle.append(line)

    rowSum = []
    for i in xrange(L):
        line = []
        for j in xrange(i + 1):
            if j == 0:
                line.append(triangle[i][j])
            else:
                line.append(line[-1] + triangle[i][j])
        rowSum.append(line)

    ans = 0
    for i in xrange(L):
        for j in xrange(i + 1):
            curSum = 0
            for k in xrange(i, L):
                if j == 0:
                    curSum += rowSum[k][j + k - i]
                else:
                    curSum += rowSum[k][j + k - i] - rowSum[k][j - 1]
                ans = min(ans, curSum)

    print ans
