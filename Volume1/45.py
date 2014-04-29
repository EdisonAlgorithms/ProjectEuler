from math import *

def t(x) :
	return x * (x + 1) / 2

def p(x) :
	return x * (3 * x - 1) / 2

def h(x) :
	return x * (2 * x - 1)

def T(x) :
	x *= 2
	y = int(sqrt(x))
	if y * (y + 1) == x :
		return True
	else :
		return False

def P(x) :
	x *= 6
	y = int(sqrt(x))
	if y % 3 == 2 and y * (y + 1) == x :
		return True
	else :
		return False


if __name__ == '__main__' :
	i = 143
	while True :
		i += 1
		H = h(i)
		if T(H) and P(H) :
			print H
			break