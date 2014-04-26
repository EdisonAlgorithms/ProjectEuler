if __name__ == '__main__' :
	a = 1
	b = 1
	i = 2
	while True:
		c = a + b
		a = b
		b = c
		i += 1 
		if len(str(c)) == 1000 :
			print i
			break
