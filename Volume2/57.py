if __name__ == '__main__' :
	n , d, ret = 3 , 2, 0
	for i in range(2, 1001) :
		n , d = n + d * 2, n + d
		if (len(str(n)) > len(str(d))) :
			ret += 1
	print ret