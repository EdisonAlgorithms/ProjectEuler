def digit_root(x):
    if x % 9 == 0:
        return 9
    else:
        return x % 9

if __name__ == "__main__":
    L = 10 ** 6 - 1
    mdrs = [0] * (L + 1)
    for i in range(2, L + 1):
        if mdrs[i] == 0:
            mdrs[i] = digit_root(i)
        else:
            mdrs[i] = max(mdrs[i], digit_root(i))
        for j in range(2 * i, L + 1, i):
            mdrs[j] = max(mdrs[i] + mdrs[j / i], mdrs[j])
    ans = sum(mdrs)
    print ans
