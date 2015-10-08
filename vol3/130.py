def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def is_prime(n):
    for i in xrange(2, n):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

def A(n):
    if is_prime(n) or gcd(n, 10) != 1:
        return n
    x = 1
    ret = 1
    while x != 0:
        x = (x * 10 + 1) % n
        ret += 1
    return ret

if __name__ == "__main__":
    ans = []
    n = 90
    while True:
        v = A(n)
        if (n - 1) % v == 0:
            ans.append(n)
            if len(ans) == 25:
                break
        n += 1
    print sum(ans)
