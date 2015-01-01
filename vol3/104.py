def top_digits(n):
    t = n * 0.20898764024997873 + (-0.3494850021680094)
    t = int((pow(10, t - int(t) + 8)))
    return t

def is_pandigital(n):
    s = set(str(n))
    return len(s) == 9 and '0' not in s

if __name__ == "__main__":
    f0, f1 = 1, 1
    count = 2
    while True:
        f0, f1 = f1, (f0 + f1) % 10 ** 9
        count += 1
        if is_pandigital(f1) and is_pandigital(top_digits(count)):
            break
    print count
