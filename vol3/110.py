from functools import reduce

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

mult = lambda x: reduce(lambda y, z: y * z, x, 1)

trans = lambda x: mult(primes[i] ** (x[i] / 2) for i in range(len(x)))

def generator(limit):
    length = len(primes)
    l = [1] * length
    while l[length - 1] < limit:
        i = length - 1
        while i > 0 and l[i] == l[i - 1]:
            l[i] = 1
            i -= 1
        l[i] += 2
        yield l

if __name__ == "__main__":
    limit = 4 * (10 ** 6)
    print min(trans(l) for l in generator(13) if mult(l) > 2 * limit)

