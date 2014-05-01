if __name__ == '__main__' :
	i = 1
	while True :
		s0 = sorted([x for x in str(i)])
		flag = True
		for j in range(2, 7) : 
			s1 = sorted([x for x in str(i * j)])
			if s0 != s1 :
				flag = False
				break
		if flag :
			print i
			break
		i += 1