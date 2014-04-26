import sys

if __name__ == '__main__' :
	print sum(ord(i) - ord('0') for i in str(2 ** 1000))