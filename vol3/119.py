def digit_sum(x):
    return sum([ord(s) - ord('0') for s in str(x)])

if __name__ == "__main__":
    cnt = 0
    ans = []
    for i in range(2, 50):
        for j in range(2, 400):
            v = j ** i
            if digit_sum(v) == j:
                cnt += 1
                ans.append(v)
                if cnt >= 50:
                    break
        if cnt >= 50:
            break
    print sorted(ans)[29]
