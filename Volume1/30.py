if __name__ == '__main__' :
	i = 2
	ret = 0
	while True :
		if i > len(str(i)) * (9 ** 5) :
			break
		s = sum((ord(x) - ord('0')) ** 5 for x in str(i))
		if s == i :
			ret += i
		i += 1
	print ret