def is_bouncy(x):
    s = str(x)
    l = len(s)
    inc = False
    dec = False
    for i in range (1, l):
        if s[i] > s[i - 1]:
            inc = True
        if s[i] < s[i - 1]:
            dec = True
        if inc and dec:
            return True
    return False

if __name__ == "__main__":
    count, total = 0, 100
    while True:
        total += 1
        if is_bouncy(total):
            count += 1
        if total * 99 % 100 == 0 and total * 99 / 100 == count:
            break
    print total
