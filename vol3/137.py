import math

def fibonacci(x):
    sqrt5 = math.sqrt(5)
    return int((pow((1 + sqrt5) / 2, x) - pow((1 - sqrt5) / 2, x)) / sqrt5)

if __name__ == "__main__":
    k = 15
    print fibonacci(2 * k) * fibonacci(2 * k + 1)



