from decimal import getcontext, Decimal

if __name__ == '__main__':
	getcontext().prec = 102
	L = 100
	d = 100
	p = pow(10, d - 1)
	ans = 0
	for i in range(2, L):
		q = Decimal(i).sqrt()
		ans += sum(int(c) for c in str(p * q)[:d]) if q % 1 != 0 else 0
	print ans