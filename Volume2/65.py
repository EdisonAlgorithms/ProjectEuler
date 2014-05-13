if __name__ == '__main__':
	n, d, L = 2, 1, 100
	for i in range(L, 0, -1):
		n, d = d, n + d * (1 if i % 3 != 0 else 2 * i / 3)
	print sum(int(i) for i in str(d))
