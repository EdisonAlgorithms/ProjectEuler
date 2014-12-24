import math

def isPrime(x) :
	if x <= 1 :
		return False
	for i in range(2, int(math.sqrt(x)) + 1) :
		if x % i == 0 :
			return False
	return True

if __name__ == '__main__' :
	ret = 0
	for i in range(1, 1000000) :
		flag = True
		for j in range(0, len(str(i))) :
			if not isPrime(int(str(i)[j:] + str(i)[0:j])) :
				flag = False
				break
		if flag :
			ret += 1
	print ret