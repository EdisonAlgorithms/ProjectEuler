if __name__ == "__main__":
    LIMIT = 10 ** 6
    d = [1] * (LIMIT + 1)
    for i in xrange(2, LIMIT / 2):
        for j in xrange(2 * i, LIMIT, i):
            d[j] += i
    max_length = 0
    ans = 0
    for i in xrange(2, LIMIT):
        n, chain = i, []
        while d[n] <= LIMIT:
            d[n], n = LIMIT + 1, d[n]
            try:
                k = chain.index(n)
            except ValueError:
                chain.append(n)
            else:
                if len(chain[k:]) > max_length:
                    max_length = len(chain[k:])
                    ans = min(chain[k:])
    print ans
