LIMIT = 200

def search(power, depth):
    if power > LIMIT or depth > cost[power]:
        return
    cost[power] = depth
    path[depth] = power
    for i in range(depth, -1, -1):
        search(power + path[i], depth + 1)

if __name__ == "__main__":
    cost = [LIMIT + 1] * (LIMIT + 1)
    path = [0] * (LIMIT + 1)
    cost[0] = 0
    search(1, 0)
    print sum(cost)
