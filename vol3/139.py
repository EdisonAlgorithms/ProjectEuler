import math

if __name__ == "__main__":
    L = 100 * (10 ** 6)
    ans = 0
    x = 1
    y = 1
    while x + y < L:
        x, y = 3 * x + 4 * y, 2 * x + 3 * y
        ans += L / (x + y)
    print ans
