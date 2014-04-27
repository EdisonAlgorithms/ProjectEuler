if __name__ == '__main__' :
	m = [1, 2, 5, 10, 20, 50, 100, 200];
	ret = [0 for i in range(0, 201)]
	ret[0] = 1
	for j in m :
		for i in range(j, 201) :
			ret[i] += ret[i - j]
	print ret[200]