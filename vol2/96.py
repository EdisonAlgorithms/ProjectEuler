import urllib2

def same_row(i,j): return (i/9 == j/9)
def same_col(i,j): return (i-j) % 9 == 0
def same_block(i,j): return (i/27 == j/27 and (i % 9)/3 == (j % 9)/3)

def solve(x):
    i = x.find('0')
    if i == -1:
        return int(x[0:3])

    ex = set()
    for j in range(81):
        if same_row(i,j) or same_col(i,j) or same_block(i,j):
            ex.add(x[j])

    for m in '123456789':
        if not m in ex:
            ret = solve(x[:i] + m + x[i + 1:])
            if ret != 0:
                return ret

    return 0

if __name__ == "__main__":
    file = urllib2.urlopen('https://projecteuler.net/project/resources/p096_sudoku.txt').readlines()
    s = []
    cur = []
    for line in file:
        if not 'Grid' in line:
            cur.append(line[:9])
        if len(cur) == 9:
            s.append(''.join(x for x in cur))
            cur = []
    print sum(solve(x) for x in s)
