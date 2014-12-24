import sys

if __name__ == '__main__' :
	s = sorted(str(sys.stdin.readline())[1:-1].split("\",\""))
	size = len(s)
	ret = 0
	for i in range(size) :
		ret += sum(ord(i) - ord('A') + 1 for i in s[i]) * (i + 1)
	print ret