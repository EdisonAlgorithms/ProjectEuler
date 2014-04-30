import math

def isPrime(x) :
	if x <= 1 :
		return False
	for i in range(2, int(math.sqrt(x)) + 1) :
		if x % i == 0 :
			return False
	return True

if __name__ == '__main__' :
	i = 1
	while True :
		num = [0, 0, 0, 0]
		flag = False
		for k in range(0, 4) :
			t = i + k
			for j in range(2, int(math.sqrt(t)) + 1) :
				if t % j == 0 :
					num[k] += 1
					while t % j == 0 :
						t /= j
			if t != 1 :
				num[k] += 1
			if num[k] != 4 :
				break
			if k == 3 :
				flag = True
		if flag :
			break
		i += 1
	print i
