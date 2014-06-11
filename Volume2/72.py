if __name__ == '__main__':
	L = 1000000
	phi = range(L + 1)
	for i in range(2, L + 1):
		if phi[i] == i:
			for k in xrange(i, L + 1, i):
				phi[k] = phi[k] / i * (i - 1)
	print sum(phi) - 1