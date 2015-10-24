import time

def ulam(a, b):
	yield a
	yield b
	u = [a, b]
	even_element = 0
	while even_element == 0 or u[-1] < 2 * even_element:
		sums = {}
		for i in range(len(u)):
			for j in range(i + 1, len(u)):
				sums[u[i] + u[j]] = sums.get(u[i] + u[j], 0) + 1
		u.append(min(k for k, v in sums.iteritems() if v == 1 and k > u[-1]))
		yield u[-1]
		if u[-1] % 2 == 0:
			even_element = u[-1]
	index = 0
	while even_element + u[index] <= u[-1]:
		index += 1
	while True:
		if even_element + u[index] > u[-1] + 2:
			u.append(u[-1] + 2)
		else:
			u.append(even_element + u[index + 1])
			index = index + 2
		yield u[-1]

if __name__ == "__main__":
	N = 10 ** 11
	ans = 0
	periods = [32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152]
	diffs = [126, 126, 1778, 6510, 23622, 510, 507842, 1523526, 8388606]
	for n in range(2, 11):
		u = ulam(2, 2 * n + 1)
		index = 0
		even = False
		while not even or (N - index) % periods[n - 2] != 0:
			num = u.next()
			if num % 2 == 0 and num > 2:
				even = True
			index += 1
		ans += num + (N - index) / periods[n - 2] * diffs[n - 2]
	print ans