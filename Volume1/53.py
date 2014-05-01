def factorial(x) :
	ret = 1
	for i in range(2, x + 1) :
		ret *= i
	return ret

if __name__ == '__main__' :
	s = [factorial(x) for x in range(101)]
	ret = 0
	for i in range(2, 101) :
		for j in range(0, i + 1) :
			c = s[i] / s[j] / s[i - j]
			if c > 1000000 :
				ret += 1
	print ret
