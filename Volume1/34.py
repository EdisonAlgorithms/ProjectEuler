import math

if __name__ == '__main__' :
	ret = 0
	factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
	upper = 1
	i = 1
	while True:
		upper *= 10
		if math.log(362880) + math.log(i) < i * math.log(10) :
			break
		i += 1
	print upper
	i = 10
	while i < upper:
		print i
		temp = sum(factorial[ord(x) - ord('0')] for x in str(i))
		if temp == i :
			ret += i
		i += 1
	print ret