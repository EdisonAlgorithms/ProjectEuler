def factorial(x):
    ret = 1
    for i in range(2, x + 1):
        ret *= i
    return ret

def choose(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)


if __name__ == "__main__":
    n = 100
    print choose(n + 9, 9) + choose(n + 10, 10) - 2 - 10 * n
