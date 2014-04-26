def factorial(n) :
	ret = 1
	for i in range(2, n + 1) :
		ret *= i
	return ret

if __name__ == '__main__' :
	order = 1000000
	order -= 1
	ret = ''
	s = [i for i in range(0, 10)]
	for i in range(1, 11) :
		ret += str(s[order / factorial(10 - i)])
		del s[order / factorial(10 - i)]
		order %= factorial(10 - i)
	print ret