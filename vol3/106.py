def factorial(x):
    ret = 1
    for i in range(2, x + 1):
        ret *= i
    return ret

def choose(n, k):
    return factorial(n) / factorial(k) / factorial(n - k)

def catalan(n):
    return choose(2 * n, n) / (n + 1)

if __name__ == "__main__":
    n = 12
    print sum(choose(n, i) * choose(n - i, i) / 2 - choose(n, 2 * i) * catalan(i) for i in range(2, n / 2 + 1))

