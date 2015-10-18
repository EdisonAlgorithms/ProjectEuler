from utils.primes import get_primes, is_prime
import math

def check(num):
	if '200' not in str(num):
		return False
	for i in xrange(len(str(num))):
		for j in range(0, 10):
			new_num = int(str(num)[:i] + str(j) + str(num)[i + 1:])
			if is_prime(new_num):
				return False
	return True


if __name__ == "__main__":
	L = 10 ** 12
	primes = get_primes(int(math.sqrt(L)))
	q_upperbound = int((L / 4) ** (1.0 / 3))
	ans = []
	for q in primes:
		if q > q_upperbound:
			break
		p_upperbound = int((L / (q ** 3)) ** (1.0 / 2))
		for p in primes:
			if p > p_upperbound:
				break
			if p == q:
				continue
			num = (p ** 2) * (q ** 3)
			if check(num):
				ans.append(num)
	print sorted(ans)[199]