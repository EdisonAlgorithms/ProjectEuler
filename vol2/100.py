if __name__ == "__main__":
    b, n, L = 85, 120, 10 ** 12
    while n <= L:
        b, n = 3 * b + 2 * n - 2, 4 * b + 3 * n - 3
    print b, n
