import math

def isPrime(x) :
	if x <= 1 :
		return False
	for i in range(2, int(math.sqrt(x)) + 1) :
		if x % i == 0 :
			return False
	return True

if __name__ == '__main__' :
	i = 9
	while True :
		flag = False
		if not isPrime(i) :
			for j in range(1, int(math.sqrt(i / 2)) + 1) :
				if i >= 2 * j * j and isPrime(i - 2 * j * j) :
					flag = True
					break 
			if not flag :
				break
		i += 2
	print i
