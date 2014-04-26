if __name__ == "__main__" :
	number = 1
	for i in range(2, 101) :
		number *= i;
	print sum(ord(i) - ord('0') for i in str(number))