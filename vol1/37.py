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
	num = 0
	i = 10
	while num < 11 :
		flag = True
		for j in range(0, len(str(i))) :
			if (not isPrime(int(str(i)[j:]))) or (not isPrime(int(str(i)[:len(str(i)) - j]))) :
				flag = False
				break
		if flag :
			ret += i
			num += 1
			print i
		i += 1
	print ret