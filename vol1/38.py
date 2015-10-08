if __name__ == '__main__' :
	i = 1
	ret = 0
	while True :
		s = ''
		j = 1
		while len(s) < 9 :
			s += str(i * j)
			j += 1
		if len(s) == 9 :
			ss = set(k for k in s)
			if len(ss) == 9 and '0' not in ss :
				if ret < int(s) :
					ret = int(s)
				print ret
		if len(s) > 9 and j == 3 :
			break
		i += 1
	print ret