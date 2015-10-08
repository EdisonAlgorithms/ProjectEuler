from itertools import combinations, product
from urllib2 import urlopen
from math import ceil

def powerset(s):
    ret = []
    for r in range(1, len(s) + 1):
        for j in combinations(s, r):
            ret.append(list(j))
    return ret

def check_cond1(s):
    d = set()
    for i in powerset(s):
        if sum(i) in d:
            return False
        else:
            d.add(sum(i))
    return True

def check_cond2(s):
    if len(s) % 2 == 1:
        up = len(s) / 2 + 1
    else:
        up = len(s) / 2
    for i in range(2, up + 1):
        if sum(s[:i]) <= sum(s[-(i - 1):]):
            return False
    return True

if __name__ == "__main__":
    current = [20, 31, 38, 39, 40, 44, 46]
    ans = sum(current)
    for i in product(*[list(range(x - 3, x + 4)) for x in current]):
        l = list(i)
        if sum(l) >= ans:
            continue
        elif check_cond2(l) and check_cond1(l):
            current = l
            ans = sum(current)
    print "".join(str(x) for x in sorted(current))
