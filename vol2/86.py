import math

if __name__ == "__main__":
        count = 0
        target = 10 ** 6
        l = 2
        while count < target:
            l += 1
            for wh in range(3, 2 * l + 1):
                d = int(math.sqrt(wh * wh + l * l))
                if wh * wh + l * l == d * d:
                    if wh <= l:
                        count += wh / 2
                    else:
                        count += 1 + (l - (wh + 1) / 2)
        print l
