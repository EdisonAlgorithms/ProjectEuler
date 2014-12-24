import math

ret = 0
v = [False for i in range(10)]

def isPrime(x) :
	if x <= 1 :
		return False
	for i in range(2, int(math.sqrt(x)) + 1) :
		if x % i == 0 :
			return False
	return True

def dfs(l, x) :
	if l == 7:
		if isPrime(x) :
			global ret
			if x > ret :
				ret = x
	for i in range(1, 8) :
		if not v[i] :
			v[i] = True
			dfs(l + 1, x * 10 + i)
			v[i] = False

if __name__ == '__main__' :
	dfs(0, 0)
	print ret