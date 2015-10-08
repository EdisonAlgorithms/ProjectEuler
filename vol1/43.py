v = [False for i in range(0, 10)]
ret = 0
div = [2, 3, 5, 7, 11, 13, 17]

def isSubDiv(x) :
	for i in range(1, 8) :
		sub = int(str(x)[i:i + 3])
		if sub % div[i - 1] != 0 :
			return False
	return True

def dfs(l, x) :
	if l == 10:
		if isSubDiv(x) :
			global ret
			ret += x
	for i in range(0, 10) :
		if not v[i] :
			v[i] = True
			dfs(l + 1, x * 10 + i)
			v[i] = False


if __name__ == '__main__' :
	dfs(0, 0)
	print ret