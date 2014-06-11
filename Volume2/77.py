if __name__ == '__main__':
	primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79]
	ret = 11
	while True:
		dp = [1] + [0] * ret
		for p in primes:
			for i in range(p, ret + 1):
				dp[i] += dp[i - p]
		if dp[ret] > 5000:
			break
		ret += 1
	print ret

