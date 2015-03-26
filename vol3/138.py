if __name__ == "__main__":
    ans = 0
    x = 0
    y = 1
    for i in range(12):
        x, y = -9 * x - 4 * y - 4, -20 * x - 9 * y - 8
        ans += abs(y)
    print ans
