from utils import get_primes, is_prime

def get_number(x, y):
	if y > x or x < 0 or y < 0:
		return 0
	return x * (x - 1) / 2 + y

def is_triplet(x, y):
	if not is_prime(get_number(x, y)):
		return False

	cnt = 0
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
	for dx, dy in directions:
		xx, yy = x + dx, y + dy
		if is_prime(get_number(xx, yy)):
			cnt += 1
			for dxx, dyy in directions:
				if dxx == -dx and dyy == -dy:
					continue
				xxx, yyy = xx + dxx, yy + dyy
				if is_prime(get_number(xxx, yyy)):
					return True
		if cnt >= 2:
			return True

	return False


if __name__ == "__main__":
	N = [5678027, 7208785]
	ans = 0
	for n in N:
		for i in range(1, n + 1):
			print i, n
			if is_triplet(n, i):
				ans += get_number(n, i)
	print ans