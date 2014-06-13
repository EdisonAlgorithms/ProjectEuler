from urllib2 import urlopen

if __name__ == '__main__':
	file_url = 'http://projecteuler.net/project/matrix.txt'
	rows = [map(int, row.split(',')) for row in urlopen(file_url).readlines()]
	n = len(rows)

	for i in range(n):
		for j in range(n):
			if i > 0 and j > 0:
				rows[i][j] += min(rows[i - 1][j], rows[i][j - 1])
			elif i > 0:
				rows[i][j] += rows[i - 1][j]
			elif j > 0:
				rows[i][j] += rows[i][j - 1]

	print rows[n - 1][n - 1]