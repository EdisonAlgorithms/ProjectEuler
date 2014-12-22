def getCircle(d) :
	for i in range(1, d) :
		if 10 ** i % d == 1 :
			return i

if __name__ == '__main__' :
	longest = max(getCircle(i) for i in range(2, 1001))
	print [i for i in range(2, 1001) if getCircle(i) == longest]