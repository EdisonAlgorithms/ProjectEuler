if __name__ == "__main__":
    ans = 0
    L = 51
    for x1 in range(0, L):
        for y1 in range(0, L):
            if x1 != 0 or y1 != 0:
                for x2 in range(0, L):
                    for y2 in range(0, L):
                        if x2 == 0 and y2 == 0:
                            continue
                        if x2 == x1 and y1 == y2:
                            continue
                        if (x1 == 0 and y2 == 0) or (x2 == 0 and y1 == 0):
                            pass
                        elif y2 * x1 == y1 * x2:
                            continue
                        d1 = (x1 ** 2) + (y1 ** 2)
                        d2 = (x2 ** 2) + (y2 ** 2)
                        d3 = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
                        d = d1 + d2 + d3
                        if max(d1, d2, d3) * 2 == d:
                            ans += 1
    print ans / 2
