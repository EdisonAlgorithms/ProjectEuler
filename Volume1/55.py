if __name__ == '__main__' :
	ret = 0
	for i in range(1, 10001) :
		flag = False
		j = 0
		num = i
		while not flag and j < 50 :
			num = num + int(str(num)[::-1])
			if str(num) == str(num)[::-1] :
				flag = True
			j += 1
		if not flag :
			ret += 1
	print ret