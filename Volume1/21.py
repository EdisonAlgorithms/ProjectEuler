def sumOfDivisor(n) :
	return sum([i for i in range(1, n) if n % i == 0])

if __name__ == '__main__' :
	sumList = [i for i in range(1, 10001) if sumOfDivisor(sumOfDivisor(i)) == i]
	print sum(i for i in sumList if sumOfDivisor(i) != i)