if __name__ == '__main__' :
	num1 = num2 = 1
	for a in range(1, 10) :
		for b in range(a + 1, 10) :
			if (10 * a * b) % (9 * a + b) == 0 :
				x = (10 * a * b) / (9 * a + b)
				num1 *= a
				num2 *= x
	t = num2
	while num1 % num2 != 0 :
		temp = num1;
		num1 = num2;
		num2 = temp % num2
	print t / num2