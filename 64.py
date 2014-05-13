from math import sqrt

if __name__ == '__main__':
	L = 10000
	for i in range(2, L + 1):
		r = int(sqrt(i))
		if r * r == i:
			continue
		k, period = 1, 0
		while k != 1 or period == 0:
			k = (N - r * r) / k
			