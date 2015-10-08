if __name__ == "__main__":
    L = 30
    sqrt5 = 5 ** 0.5
    f = [7, 14, 50, 97]
    for i in range(L - 4):
        f.append(7 * f[-2] - f[-4])
    print sum(int(x / sqrt5) - 1 for x in f)
