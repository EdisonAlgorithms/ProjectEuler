from urllib2 import urlopen

if __name__ == '__main__':
	file_url = 'http://projecteuler.net/project/matrix.txt'
	rows = [map(int, row.split(',')) for row in urlopen(file_url).readlines()]
	n = len(rows)
	cost = [rows[i][0] for i in range(n)]

	for i in range(1, n):
		for j in range(n):
			cost[j] = min(cost[j], cost[j - 1]) + rows[j][i]
		for j in range(n - 2, -1, -1):
			cost[j] = min(cost[j], cost[j + 1] + rows[j][i])

	print min(cost)