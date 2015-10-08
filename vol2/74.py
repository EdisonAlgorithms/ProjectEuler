factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def sumFacDig(x):
	return sum(factorial[int(i)] for i in str(x))

def getChain(x):
	m = set([])
	while x not in m:
		m.add(x)
		x = sumFacDig(x)
	return len(m)

if __name__ == '__main__':
	ans = 0
	L = 1000000
	for i in range(2, L + 1):
		if getChain(i) == 60:
			ans += 1
	print ans