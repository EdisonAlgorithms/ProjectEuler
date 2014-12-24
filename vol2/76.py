if __name__ == '__main__':
	L = 100
	dp = [1] + [0] * L
	for i in range(1, L):
		for j in range(i, L + 1):
			dp[j] += dp[j - i]
	print dp[L] 