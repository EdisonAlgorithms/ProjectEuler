def cubes(x, y, z, n):
    return 2 * (x * y + x * z + y * z) + 4 * (x + y + z + n - 2) * (n - 1)

if __name__ == "__main__":
    LIMIT = 30000
    count = [0] * (LIMIT + 1)
    for z in xrange(1, LIMIT):
        if cubes(z, z, z, 1) > LIMIT:
            break
        for y in xrange(z, LIMIT):
            if cubes(y, y, z, 1) > LIMIT:
                break
            for x in xrange(y, LIMIT):
                if cubes(x, y, z, 1) > LIMIT:
                    break
                for n in xrange(1, LIMIT):
                    c = cubes(x, y, z, n)
                    if c > LIMIT:
                        break
                    count[c] += 1
    for i in range(1, LIMIT):
        if count[i] == 1000:
            print i
            break

