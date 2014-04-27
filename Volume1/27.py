import math

def isPrime(n) :
	if n < 0 :
		n = -n
	if n <= 1 :
		return False
	for i in range(2, int(math.sqrt(n)) + 1) :
		if n % i == 0 :
			return False
	return True

def getPrime(a, b) :
	for i in range(0, 1000) :
		if not isPrime(i * i + a * i + b) :
			return i
	return 1000

if __name__ == '__main__' :
	ret = 0
	for b in range(-999, 1000) :
		if not isPrime(b) :
			continue
		for a in range(-999, 1000) :
			if not isPrime(1 + a + b) :
				continue
			temp = getPrime(a, b)
			if temp > ret :
				ret = temp
				print a * b
