v = [0 for i in range(4)]

def dfs(l, a, s, n) :
	if l == 4 :
		s += [n]
		return
	for i in range(4) :
		if v[i] == 0 :
			v[i] = 1
			dfs(l + 1, a, s, n * 10 + a[i])
			v[i] = 0


if __name__ == '__main__' :
	prime = []
	v = [0 for i in range(0, 10001)]
	for i in range(2, 10001) :
		if v[i] == 0 :
			for j in range(2, 10000 / i + 1) :
				v[i * j] = 1
			prime += [i]
	length = len(prime)
	print length
	for i in range(length) :
		if len(str(prime[i])) == 4 :
			a = [ord(x) - ord('0') for x in str(prime[i])]
			s = []
			dfs(0, a, s, 0)
			s = sorted(set(s))
			length2 = len(s)
			for j in range(0, length2 - 2) :
				if len(str(s[j])) == 4 and s[j] in prime :
					for k in range(j + 1, length2 - 1) :
						if s[k] in prime:
							t = s[k] + s[k] - s[j]
							if t in s and t in prime :
								print str(s[j]) + str(s[k]) + str(t)




