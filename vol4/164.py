if __name__ == "__main__":
	ans = {}
	ans[3] = {}
	for a in range(0, 10):
		ans[3][a] = {}
		for b in range(0, 10 - a):
			ans[3][a][b] = 10 - a - b
	for n in range(4, 21):
		ans[n] = {}
		for a in range(0, 10):
			ans[n][a] = {}
			for b in range(0, 10 - a):
				ans[n][a][b] = 0
				for c in range(0, 10 - a - b):
					ans[n][a][b] += ans[n - 1][b][c]
	ret = 0
	for a in range(1, 10):
		for b in range(0, 10 - a):
			ret += ans[20][a][b]
	print ret