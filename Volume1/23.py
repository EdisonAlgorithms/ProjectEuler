def sumOfDivisor(n) :
	ret = 1
	for i in range(2, int(n ** 0.5) + 1) :
		if n % i == 0 :
			ret += i + n / i
			if i * i == n :
				ret -= i
	return ret

if __name__ == '__main__' :
	list = set()
	ret = 0
	for i in range(1, 28124) :
		if sumOfDivisor(i) > i :
			list.add(i)
		if not any(i - j in list for j in list) :
			ret += i
	print ret