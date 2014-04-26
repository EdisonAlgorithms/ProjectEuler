def getDays(y, m):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        return 31
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    if m == 2:
        if y % 400 == 0:
            return 29
        if y % 4 == 0 and y % 100 != 0:
            return 29
        return 28

if __name__ == '__main__' :
    sumDays = 0
    sundays = 0
    for y in range(1900, 2001):
        for m in range(1, 13):
            sumDays += getDays(y, m)
            if (sumDays + 2) % 7 == 0 and y >= 1901:
                sundays += 1
    print(sundays)