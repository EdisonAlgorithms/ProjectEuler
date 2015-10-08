import math

def is_square(n):
    sqrt_n = int(math.sqrt(n))
    return n == sqrt_n * sqrt_n

if __name__ == "__main__":
    result = 0
    i = 3
    while result == 0:
        i += 1
        a = i * i
        for j in range(3, i):
            if result != 0:
                break
            c = j * j
            f = a - c
            if not is_square(f):
                continue
            if j % 2 == 1:
                kstart = 1
            else:
                kstart = 2

            for k in range(kstart, j, 2):
                d = k * k
                e = a - d
                b = c - e

                if b <= 0 or not is_square(e) or not is_square(b):
                    continue

                x = (a + b) / 2
                y = (e + f) / 2
                z = (c - d) / 2

                result = x + y + z
                break

    print result
