from math import sqrt

def minX(d):
	m, x, y, k, sd = 1, 1, 0, 1, sqrt(d)
	while k != 1 or y == 0:
		m = k * (m / k + 1) - m
		m = m - int((m - sd) / k) * k
		xx = (x * m + d * y) / abs(k)
		yy = (x + y * m) / abs(k)
		k = (m * m - d) / k
		x = xx
		y = yy
	return x

if __name__ == '__main__':
	print max([minX(d), d] for d in range(1, 1001) if int(sqrt(d)) * int(sqrt(d)) != d)