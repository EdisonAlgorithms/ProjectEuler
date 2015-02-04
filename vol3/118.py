from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    for i in xrange(2, x):
        if i * i > x:
            break
        if x % i == 0:
            return False
    return True

def check_partition(perm, start, prev):
    ret = 0
    n = len(perm)
    number = 0
    for i in range(start, n):
        number = number * 10 + perm[i]
        if number < prev:
            continue
        if not is_prime(number):
            continue
        if i == n - 1:
            return ret + 1
        ret += check_partition(perm, i + 1, number)
    return ret

if __name__ == "__main__":
    ans = 0
    for p in permutations(range(1, 10)):
        ans += check_partition(list(p), 0, 0)
    print ans
