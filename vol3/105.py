from itertools import combinations
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
    sets = []
    for l in urlopen('https://projecteuler.net/project/resources/p105_sets.txt'):
        s = sorted(map(int, l.strip().split(',')))
        sets.append(s)
    print sum(sum(s) for s in sets if check_cond2(s) and check_cond1(s)) 

