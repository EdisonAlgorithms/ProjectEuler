if __name__ == '__main__' :
	num = 1
	ret = 1
	for i in range(1, 7) :
		num = 10 ** i
		temp = 0
		while num > 9 * (10 ** temp) * (temp + 1) :
			num -= 9 * (10 ** temp) * (temp + 1)
			temp += 1
		num -= 1
		t1 = (10 ** temp) + num / (temp + 1)
		t2 = num % (temp + 1)
		ret *= int(str(t1)[t2])
	print ret
