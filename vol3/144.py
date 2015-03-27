import math

if __name__ == "__main__":
    ans = 0
    x0, y0 = 0.0, 10.1
    x1, y1 = 1.4, -9.6
    while True:
        slope1, slope = (y1 - y0) / (x1 - x0), -4 * x1 / y1
        tan1 = (slope1 - slope) / (1 + slope1 * slope)
        
        slope2 = (slope - tan1) / (1 + slope * tan1)
        intercept2 = y1 - slope2 * x1

        a, b, c = 4 + slope2 * slope2, 2 * slope2 * intercept2, intercept2 * intercept2 - 100

        ans1, ans2 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a), (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

        x0, y0 = x1, y1

        if abs(ans1 - x1) > abs(ans2 - x1):
            x1 = ans1
        else:
            x1 = ans2
        y1 = slope2 * x1 + intercept2

        ans += 1
        if abs(x1) < 0.01 and y1 > 0:
            break

    print ans
        
