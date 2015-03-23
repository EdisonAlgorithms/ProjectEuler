import math

def count_digit(x):
    return int(math.ceil(math.log(x + 1, 10)))

def extended_gcd(a, b):
    x = 0
    lastx = 1
    y = 1
    lasty = 0
    while b != 0:
        q = a / b

        tmp = b
        b = a % b
        a = tmp

        tmp = x
        x = lastx - q * x
        lastx = tmp

        tmp = y
        y = lasty - q * y
        lasty = tmp
    return lastx, lasty, a

if __name__ == "__main__":
    L = 1000000
    p = [0] * (L + 100)
    prime = []
    for i in range(2, L + 100):
        if p[i] == 0:
            for j in range(2 * i, L + 100, i):
                p[j] = 1
            prime.append(i)
   
    ans = 0
    for i in range(len(prime)):
        if prime[i] < 5:
            continue
        if prime[i] >= L:
            break
        p1 = prime[i]
        p2 = prime[i + 1]

        a = 10 ** (count_digit(p1))
        b = p2 - p1
        n = p2
        
        x, y, r = extended_gcd(a, n)
        res = (x * b) % n
        
        ans += a * res + p1

    print ans

