def isPalindrome(x):
    s = str(x)
    l = len(s)
    for i in range(0, l / 2):
        if s[i] != s[l - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    LIMIT = 10 ** 8
    i = 1
    ans = set()
    while i * i <= LIMIT:
        cur = i * i
        j = i + 1
        while cur + j * j <= LIMIT:
            cur += j * j
            if isPalindrome(cur):
                ans.add(cur)
            j += 1
        i += 1
    print sum(ans)
