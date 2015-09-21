import fractions

def calc(m):
    ret = 1
    for i in range(2, m + 1):
        ret *= pow(i, i)
    return ret * pow(fractions.Fraction(2, m + 1), m * (m + 1) / 2)

if __name__ == "__main__":
    L = 15
    ans = 0
    for m in range(2, L + 1):
        ans += int(calc(m))
    print ans
