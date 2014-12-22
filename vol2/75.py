from math import sqrt

def gcd(a, b):
	if a % b == 0:
		return b
	return gcd(b, a % b)

if __name__ == '__main__':
	L = 1500000
	sL = int(sqrt(L))
	tx = [0] * L
	for i in range(1, sL, 2):
		for j in range(2, sL - i, 2):
			if gcd(i, j) == 1:
				sum = abs(j * j - i * i) + 2 * i * j + j * j + i * i
				for s in range(sum, L, sum):
					tx[s] += 1
	print tx.count(1)