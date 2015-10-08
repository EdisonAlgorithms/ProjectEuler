from urllib2 import urlopen

if __name__ == "__main__":
    lines = urlopen('https://projecteuler.net/project/resources/p107_network.txt').readlines()
    n = len(lines)
    graph = []
    total = 0
    for i in range(n):
    	l = lines[i].strip().split(',')
    	e = []
    	for j in range(n):
    	    if l[j] != '-':
    		total += int(l[j])	
                e.append(float(int(l[j])))
    	    else:
    		e.append(float('inf'))
    	graph.append(e)
    dist = [graph[0][i] for i in range(n)]
    s = set([0])
    ans = 0
    for i in range(n - 1):
    	min_cost = float('inf')
    	index = -1
    	for j in range(n):
    	    if j not in s and dist[j] < min_cost:
    		min_cost = dist[j]
    		index = j
    	ans += min_cost
    	s.add(index)
    	for j in range(n):
    	    if j not in s and dist[j] > graph[index][j]:
    		dist[j] = graph[index][j]
    print total / 2 - int(ans)
