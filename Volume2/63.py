from math import log10

if __name__ == '__main__':
	ret = 0
	for i in range(1, 10):
		ret += int(1 / (1 - log10(i)))
	print ret