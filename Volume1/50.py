if __name__ == '__main__' :
	prime = []
	v = [0 for i in range(0, 1000001)]
	for i in range(2, 1000001) :
		if v[i] == 0 :
			for j in range(2, 1000000 / i + 1) :
				v[i * j] = 1
			prime += [i]
	length = len(prime)
	print length
	s = [0 for i in range(0, length + 1)]
	for i in range(1, length + 1) :
		s[i] = s[i - 1] + prime[i - 1]
	for k in range(1000, 0, -1) :
		flag = False
		for i in range(0, length + 1 - k) :
			t = s[i + k] - s[i]
			if t < 1000000 and t in prime :
				print t
				flag = True
				break
		if flag :
			break

