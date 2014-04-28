if __name__ == '__main__' :
	ret = 0
	num = 0
	for p in range(3, 1001) :
		temp = 0
		for i in range(1, p / 3) :
			for j in range(i, p * 2 / 3 - i) :
				k = p - i - j
				if i * i + j * j == k * k :
					temp += 1
		if temp > num :
			num = temp
			ret = p
		print p
	print ret