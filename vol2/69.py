if __name__ == '__main__':
	L = 10 ** 6
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
	ret = 1
	for p in primes:
		if ret * p > L:
			break
		ret *= p
	print ret