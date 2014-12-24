from math import sqrt

if __name__ == '__main__':
	L = 10000
	odd_period = 0
	for i in range(2, L + 1):
		r = limit = int(sqrt(i))
		if r * r == i:
			continue
		k, period = 1, 0
		while k != 1 or period == 0:
			k = (i - r * r) / k
			r = ((limit + r) / k) * k - r
			period += 1
		if period % 2 == 1:
			odd_period += 1
	print odd_period