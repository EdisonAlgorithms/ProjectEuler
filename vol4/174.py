if __name__ == "__main__":
    L = 10 ** 6
    count = [0] * (L + 1)
    for inner in range(1, L / 4 + 1):
        outer = inner + 2
        used = outer * outer - inner * inner
        while used <= L:
            count[used] += 1
            outer += 2
            used = outer * outer - inner * inner
    print sum(map(lambda x: 1 if 1 <= x <= 10 else 0, count))
