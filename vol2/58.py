import math

def isPrime(x) :
	if x <= 1 :
		return 0
	for i in range(2, int(math.sqrt(x)) + 1) :
		if x % i == 0 :
			return 0
	return 1

if __name__ == '__main__' :
		num, avg, n, d = 0, 1, 2, 1
		while avg >= 0.10 :
			num += isPrime(d + n) + isPrime(d + n * 2) + isPrime(d + n * 3);
			d += n * 4
			avg = num / (2.0 * n + 1)
			n += 2
		print n - 1