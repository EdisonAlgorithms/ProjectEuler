def gcd(a, b):
	if a % b == 0:
		return b
	return gcd(b, a % b);

if __name__ == '__main__':
	L = 12000
	ret = 0
	for i in range(5, L + 1):
		for j in range(i / 3 + 1, (i - 1) / 2 + 1):
			if gcd(i, j) == 1:
				ret += 1
	print ret