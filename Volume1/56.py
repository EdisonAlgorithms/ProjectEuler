if __name__ == '__main__' :
	ret = 0
	for a in range(1, 100) :
		for b in range(1, 100) :
			temp = sum([int(x) for x in str(a**b)])
			if temp > ret :
				ret = temp
	print ret