if __name__ == "__main__":
    ans = 0
    for i in range(1, 10):
        if i % 4 == 0 or i % 4 == 2:
            ans += 20 * pow(30, i / 2 - 1)
        elif i % 4 == 3:
            ans += 100 * pow(500, i / 4)
    print ans
