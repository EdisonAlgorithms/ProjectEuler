import math
def isPrime(x) :
	if x <= 1 :
		return False
	for i in range(2, int(math.sqrt(x)) + 1) :
		if x % i == 0 :
			return False
	return True

if __name__ == '__main__' :
	limit = 10000
	prime = []
	v = [0 for i in range(0, limit + 1)]
	for i in range(2, limit + 1) :
		if v[i] == 0 :
			for j in range(2, limit / i + 1) :
				v[i * j] = 1
			prime += [i]
	length = len(prime)
	print length
 
	px = dict()
	pi = 1
	for pi in range(1, length):
	  	p = prime[pi]
	  	if p == 5:
	  		continue
  		px[p] = set()
		for qi in range(pi, length):
			q = prime[qi]
			if isPrime(int(str(p) + str(q))) and isPrime(int(str(q) + str(p))):
				px[p].add(q)
 	
 	ret = -1
	for xx in px:
	  for axx in px[xx]:
	    set_a = px[xx] & px[axx]
	    if len(set_a) > 0:
	      for bxx in set_a:
	        set_b = set_a & px[bxx]
	        if len(set_b) > 0:
		  		for cxx in set_b:
		  			set_c = set_b & px[cxx]
		    		if len(set_c) > 0:
		    			for dxx in set_c :
		    				temp = xx + axx + bxx + cxx + dxx
		    				if ret == -1 or ret > temp :
		    					ret = temp
	print ret