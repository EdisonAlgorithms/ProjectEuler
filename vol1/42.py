import sys

if __name__ == '__main__' :
	words = str(sys.stdin.readline())[1:-1].split("\",\"")
	tri = [0]
	for i in range(1, 1000) :
		tri += [tri[i - 1] + i]
	ret = 0
	for word in words :
		s = sum(ord(i) - ord('A') + 1 for i in word)
		if s in tri :
			ret += 1
	print ret
