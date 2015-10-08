def A(n):
    if n % 5 == 0:
        return 1
    x = 1
    ret = 1
    while x != 0:
        x = (x * 10 + 1) % n
        ret += 1
    return ret

if __name__ == "__main__":
    LIMIT = 10 ** 6
    i = LIMIT + 1
    while A(i) <= LIMIT:
        i += 2
    print i 
