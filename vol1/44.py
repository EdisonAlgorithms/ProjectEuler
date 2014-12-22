from math import *

def f(x) :
	return x * (3 * x - 1) / 2

def g(x) :
    x *= 6  
    m = int(sqrt(x))  
    if m % 3 == 2 and m * (m + 1) == x :  
        return True
    else:  
        return False

if __name__ == '__main__' :
	ret = 0
	k = 0
	while ret == 0 :
		k += 1
		t = f(k)
		j = k - 1
		while j > 0 and ret == 0 :
			s = f(j)
			if g(t + s) and g(t - s) :
				ret = t - s
			j -= 1
	print ret

