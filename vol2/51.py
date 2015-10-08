import math

def is_prime(n):
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False
    for j in xrange(3, math.sqrt(n) + 1, 2):
        if n % j == 0:
            return False
    return True

def get_digits(n):
    return map(lambda x: int(x), set(list(str(n))))

def repl_digit(n, old, new):
    return int(str(n).replace(str(old), str(new)))

if __name__ == '__main__' :
	prime = []
	v = [0 for i in range(0, 1000001)]
	for i in range(2, 1000001) :
		if v[i] == 0 :
			for j in range(2, 1000000 / i + 1) :
				v[i * j] = 1
			prime += [i]
	length = len(prime)
	flag = False
	for i in prime :
		if i < 56000 :
			continue
		print i
		if flag :
			break
		for digit in get_digits(i) :
			found = [i]
			for repl in range(10) :
				if repl != digit :
					possible = repl_digit(i, digit, repl)
					if len(str(possible)) == len(str(i)) and possible in prime :
						found.append(possible)
			if len(found) == 8:
				print found
				flag = True
        		break
