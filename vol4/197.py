# import matplotlib.pyplot as plt

def u(n):
    f = lambda x: int(2 ** (30.403243784 - x * x)) * 1e-9
    return -1 if n == 0 else f(u(n - 1))

if __name__ == "__main__":
    i = 0
    while abs(u(i + 2) - u(i)) > 1e-10:
        i += 101
    print u(i) + u(i + 1)
