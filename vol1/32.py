if __name__ == '__main__' :
	ret = set()
	for i in range(1, 100) :
		j = i
		while True :
			s = str(i) + str(j) + str(i * j)
			if len(s) > 9:
				break;
			t = set(x for x in s)
			if '0' not in t and len(t) == 9 :
				ret.add(i * j)
			j += 1
	print sum(ret)
	print ret