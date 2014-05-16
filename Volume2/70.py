from math import sqrt

def isPerm(a, b):
	return sorted(str(a)) == sorted(str(b))

def calc(L):
	prime = []
	LL = int(1.30 * sqrt(L))
	v = [0 for i in range(0, LL + 1)]
	for i in range(2, LL + 1) :
		if v[i] == 0 :
			for j in range(2, LL / i + 1) :
				v[i * j] = 1
			prime += [i]

	min_q, min_n, i = 2, 2, 0
	for p1 in prime:
		i += 1
		for p2 in prime[i:]:
			if (p1 + p2) % 9 != 1:
				continue
			n = p1 * p2
			if n > L:
				return min_n
			phi = (p1 - 1) * (p2 - 1)
			q = n / float(phi)
			if isPerm(phi, n) and min_q > q:
				min_q, min_n = q, n

	return "WTF"

if __name__ == '__main__':
	L = 10 ** 7
	print calc(L)
	
