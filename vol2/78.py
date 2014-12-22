if __name__ == '__main__':
	k = sum([[i * (3 * i - 1) / 2, i * (3 * i - 1) / 2 + i] for i in range(1, 250)], [])
	n = 0
	m = 1e6
	p = [1]
	sgn = [1, 1, -1, -1]
	while p[n] > 0:
		n += 1
		px = 0
		i = 0
		while k[i] <= n:
			px += p[n - k[i]] * sgn[i % 4]
			i += 1
		p.append(px % m)
	print n