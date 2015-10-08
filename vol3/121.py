if __name__ == "__main__":
    LIMIT = 15    
    res = [0] * (LIMIT + 1)
    res[LIMIT - 1] = res[LIMIT] = 1
    for i in range(2, LIMIT + 1):
        for j in range(0, LIMIT):
            res[j] = res[j + 1]
        res[LIMIT] = 0
        for j in range(LIMIT, 0, -1):
            res[j] += res[j - 1] * i
    pos = 0
    for i in range(0, LIMIT / 2 + 1):
        pos += res[i]
    total = 1
    for i in range(2, LIMIT + 2):
        total *= i
    print total / pos
