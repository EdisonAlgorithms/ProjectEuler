import urllib2

if __name__ == '__main__':
	file_url = 'http://projecteuler.net/project/triangle.txt'
	table = [[int(n) for n in s.split()] for s in urllib2.urlopen(file_url).readlines()]
	print len(table)
	for row in range(len(table) - 1, 0, -1):
		for col in range(0, row):
			table[row - 1][col]	+= max(table[row][col], table[row][col + 1]);
	print table[0][0]
