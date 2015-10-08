def tld(x):
    return [x[i] - x[i - 1] for i in range(1, len(x))]

if __name__ == "__main__":
    u = lambda n : 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
    k = 10
    seq = [map(u, range(1, k + 1))]
    for i in range(k - 1):
        seq += [tld(seq[-1])]
    print sum(sum(seq, []))
