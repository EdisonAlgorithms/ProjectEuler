from math import sqrt

if __name__ == '__main__':
	L = 2000000
	x = 2
	y = L * 4 / 6
	min_diff = float('Inf')
	while x < y:
		diff = abs(x * (x + 1) * y * (y + 1) / 4 - L)
		if diff < min_diff:
			min_diff = diff
			area = x * y
		x += 1
		y = int(sqrt(L * 4 / (x * (x + 1))))
	print area